from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
# driver.get("https://www.amazon.com")

# driver.get("https://www.amazon.com/Cybertela-Ukraine-T-Shirt-Royal-X-Large/dp/B00VFBL49O/")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# price = float(price_dollar.text + "." + price_cent.text)
# print(price)

# driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# search_bar.send_keys("python")
# # search_bar.send_keys(Keys.RETURN)
# print(search_bar.get_attribute("placeholder"))

# link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(link.text)

# download_link = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div[1]/div[2]/p[2]/a")
# print(download_link.text)
# # print(driver.title)

# Challenge 1: Get the Python events and print them in a dictionary
driver.get("https://www.python.org/")
all_events = driver.find_elements(By.XPATH, value="/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul")

events = {}
num = 0
for ul in all_events:
    li_elements = ul.find_elements(By.TAG_NAME, "li")
    for li in li_elements:
        time_elem = li.find_element(By.TAG_NAME, "time")
        a_elem = li.find_element(By.TAG_NAME, "a")
        events[num] = {
            "time": time_elem.text,
            "name": a_elem.text
        }
        num += 1

print(events)

driver.quit()
