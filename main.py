from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = "YOUR_LINKEDIN_LOGIN_EMAIL"
PASSWORD = "YOUR_LINKEDIN_LOGIN_PASSWORD"
PHONE = "YOUR_PHONE_NUMBER"

chrome_driver_path = "YOUR_CHROMEDRIVER_PATH"
driver = webdriver.Chrome(chrome_driver_path)
#I use a URL taht represent python developer jobs in London. if you want anything else,
# search for it in linkedin and chang the URL
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
#Before rushing in to the next commands we must make sure that the site has loaded, i usually give it 10 secs
# but usually 5-7 will be enpogh as well
time.sleep(10)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(10)
email_field = driver.find_element_by_id("username")
email_field.send_keys(EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()


