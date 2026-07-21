from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import os
import time

# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------

# Create Chrome Profile and create account manually. Put YOUR email and password here:
ACCOUNT_EMAIL = "your_email@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "your_password"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
# Keep the browser open if the script finishes or crashes.
# If True, you need to *manually* QUIT Chrome before you re-run the script.
chrome_options.add_experimental_option("detach", True)
# Create a folder for the Chrome Profile Selenium will use every time
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
# include double -- for command line argument to Chrome
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to site
driver.get(GYM_URL)

# ----------------  Step 2 - Automated Login ----------------

# Alternative to using time.sleep(): use a standalone wait object
wait = WebDriverWait(driver, 2)

# Click login button to go to login page
login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_btn.click()

# Fill in login form
email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, "password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

# Click Login
submit_btn = driver.find_element(By.ID, "submit-button")
submit_btn.click()

# Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

# Counters for booked classes for the booking summary
booked_count = 0
waitlist_count = 0
already_booked_count = 0

# ----------------  Step 6: Book EVERY Tuesday AND Thursday 6pm class ----------------
# ----------------         and print a detailed class summary         ----------------

processed_classes = []

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday
    if "Tue" in day_title or "Thu" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            # button.click()

            # Track the class details
            class_info = f"{class_name} on {day_title}"

            # print(f"✓ Booked: {class_name} on {day_title}")

# ----------------  Step 4 - Class Booking: Checking if a class is already booked ----------------

            # Check if already booked
            # Increment the counter(s)
            if button.text == "Booked":
                print(f"✓ Already booked: {class_name} on {day_title}")
                already_booked_count += 1
                processed_classes.append(f"[Booked]: {class_info}")
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_name} on {day_title}")
                waitlist_count += 1
                processed_classes.append(f"[Waitlisted]: {class_info}")
            elif button.text == "Book Class":
                # Book the class
                button.click()
                print(f"✓ Successfully booked: {class_name} on {day_title}")
                booked_count += 1
                processed_classes.append(f"[New Booking]: {class_info}")
                # Wait a moment for the button state to update
                time.sleep(0.5)
            elif button.text == "Join Waitlist":
                # Join waitlist if class is full
                button.click()
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                waitlist_count += 1
                processed_classes.append(f"[New Waitlist]: {class_info}")
                # Wait a moment for the button state to update
                time.sleep(0.5)
            # break

# # Print summary
# print("\n--- BOOKING SUMMARY ---")
# print(f"Classes booked: {booked_count}")
# print(f"Waitlists joined: {waitlist_count}")
# print(f"Already booked/waitlisted: {already_booked_count}")
# print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")

# # Print detailed class list
# print("\n--- DETAILED CLASS LIST ---")
# for class_detail in processed_classes:
#     print(f"  • {class_detail}")

# ----------------  Step 7: Verify Class Bookings on My Bookings Page ----------------

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

# Navigate to My Bookings page
my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()

# Wait for My Bookings page to load
wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

# Count all Tuesday/Thursday 6pm bookings
verified_count = 0

# Find ALL booking cards (both confirmed and waitlist)
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Check if it's a Tuesday or Thursday 6pm class
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")






# Getting a SessionNotCreatedException?
# Remember to *Quit* Selenium's Chrome Instance before trying to click "run"



# driver.quit()
