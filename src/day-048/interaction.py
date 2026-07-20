from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# link = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[2]/section/div[1]/div/div[3]/ul/li[1]/a")
# print(link.text)
# link.click()

# search_bar = driver.find_element(By.NAME, value="search")
# print(search_bar.get_attribute("placeholder"))
# search_bar.send_keys("Python", Keys.ENTER)

driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
fname = driver.find_element(By.NAME, value="fName")
lName = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
fname.send_keys("John")
lName.send_keys("Doe")
email.send_keys("john.doe@example.com")
button = driver.find_element(By.XPATH, value="/html/body/form/button")
button.click()

driver.quit()
