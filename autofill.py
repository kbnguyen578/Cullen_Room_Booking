# ==== selenium -- autofilling on the web ====
# launch and control browser window 
from selenium import webdriver 
# locating elements on page to fill input boxes 
from selenium.webdriver.common.by import By 
# handles dropdown menus (room choices), wait until item loads before interact 
from selenium.webdriver.support.ui import Select, WebDriverWait 
# ExpCond + WebDriverWait => until element visible/clickable 
from selenium.webdriver.support import expected_conditions as ExpCond

# ==== for CHROME -- uncomment the section below & comment out Safari ====
# from webdriver_manager.chrome import ChromeDriverManager 
# from selenium.webdriver.chrome.service import Service 

URL = "https://www.egr.uh.edu/forms/room-reservation-form"
ORGANIZATION = "SASE"

def fill_form(event_data, config): 
    # ==== for CHROME ==== 
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # ==== for SAFARI -- follow instructions & uncomment line 18 & comment out Chrome ====
    # Safari > Settings > Advanced > "show features for web developers" 
    # Safari > Settings > Developer > "Allow Remote Automation "
    driver = webdriver.Safari()  

    driver.get(URL)
    wait = WebDriverWait(driver, 10)

    # field: Contact Information 
    wait.until(ExpCond.presence_of_element_located((By.NAME, "first_name")))
    # first name | name="first_name"
    driver.find_element(By.NAME, "first_name").send_keys(config["ec_first"])

    # last name | name="last_name"
    driver.find_element(By.NAME, "last_name").send_keys(config["ec_last"])

    # email | name="email_address"
    driver.find_element(By.NAME, "email_address").send_keys(config["ec_email"])

    # PSID | name="peoplesoft_id"
    driver.find_element(By.NAME, "peoplesoft_id").send_keys(config["ec_psid"])

    # Organization | name="department"
    driver.find_element(By.NAME, "department").send_keys(ORGANIZATION)

    # Phone Number | name="phone"
    driver.find_element(By.NAME, "phone").send_keys(config["ec_phone_number"])

    # field: Room is requested for 
    # first name | name="requested_for_first_name"

    # last name | name="requested_for_last_name"

    # field: Reservation Information 
    # event date | name="event_date"

    # start time | name="start_time"

    # end time | name="end_time"

    # event title | name="event_title"

    # number fo attendees | name="number_of_attendees"

    # locattion 1st choice | name="location1"

    # location 2nd choice | name="location2"

    # location 3rd choice | name="location3"

    # event description | name="description"

    input("Press Enter here once you have submitted the form...")

    driver.quit()