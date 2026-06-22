# ==== selenium -- autofilling on the web ====
# launch and control browser window 
from selenium import webdriver 
# locating elements on page to fill input boxes 
from selenium.webdriver.common.by import By 
# handles dropdown menus (room choices), wait until item loads before interact 
from selenium.webdriver.support.ui import Select, WebDriverWait 
# ExpCond + WebDriverWait => until element visible/clickable 
from selenium.webdriver.support import expected_conditions as ExpCond
import time

# ==== for CHROME -- uncomment the section below & comment out Safari ====
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service 

URL = "https://www.egr.uh.edu/forms/room-reservation-form"
ORGANIZATION = "SASE"

LOCATION_MAP = {
    "Commons (Engineering Pit)":    "Commons", 
    "W205 D3 [65]":                 "W205D3", 
    "E220 D3 [26]":                 "E220D3", 
    "102D [44]":                    "102D",
    "N61D [48]":                    "N61D", 
    "W122 D3 [124]":                "W122D3",
    "L2D2 [220]":                   "L2D2"
}

CAPACITY_MAP = {
    "Commons (Engineering Pit)":    "200", 
    "W205 D3 [65]":                 "65", 
    "E220 D3 [26]":                 "26", 
    "102D [44]":                    "44",
    "N61D [48]":                    "48", 
    "W122 D3 [124]":                "124",
    "L2D2 [220]":                   "220"
}

def fill_form(event_data, config): 
    # ==== for CHROME ==== 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # ==== for SAFARI -- follow instructions & uncomment line 18 & comment out Chrome ====
    # Safari > Settings > Advanced > "show features for web developers" 
    # Safari > Settings > Developer > "Allow Remote Automation "
    # driver = webdriver.Safari()  

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
    driver.find_element(By.NAME, "requested_for_first_name").send_keys(config["ec_first"])

    # last name | name="requested_for_last_name"
    driver.find_element(By.NAME, "requested_for_last_name").send_keys(config["ec_last"])

    """ {'title': 'Chuseok Celebration', 
    'date': '9/11/2025', 
    'desc': 'learn about chuseok, make origami hanboks, and craft traditional drums. ', 
    'start_time': '5:30:00 PM', 
    'end_time': '7:00:00 PM', 
    'loc_1': 'L2D2 [220]', 
    'loc_2': 'Commons (Engineering Pit)', 
    'loc_3': '102D [44]'} """

    # field: Reservation Information 
    # event date | name="event_date"
    driver.find_element(By.NAME, "event_date").send_keys(event_data['date'])
    print("filled date")

    # start time | name="start_time"
    driver.find_element(By.NAME, "start_time").send_keys(event_data['start_time'])
    print("filled start time")

    # end time | name="end_time"
    driver.find_element(By.NAME, "end_time").send_keys(event_data['end_time'])
    print("filled end time")

    # event title | name="event_title"
    driver.find_element(By.NAME, "event_title").send_keys(event_data['title'])
    print("filled event_title")

    # number of attendees | name="number_of_attendees"
    driver.find_element(By.NAME, "number_of_attendees").send_keys(CAPACITY_MAP[event_data['loc_1']])
    print("filled number of attendees")

    # locattion 1st choice | name="location1"
    dropdown_1 = driver.find_element(By.NAME, "location1")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_1)
    time.sleep(0.5)
    Select(dropdown_1).select_by_value(LOCATION_MAP[event_data['loc_1']])
    print("filled location 1")

    # location 2nd choice | name="location2"
    Select(driver.find_element(By.NAME, "location2")).select_by_value(LOCATION_MAP[event_data['loc_2']])
    print("filled location 2")

    # location 3rd choice | name="location3"
    Select(driver.find_element(By.NAME, "location3")).select_by_value(LOCATION_MAP[event_data['loc_3']])
    print("filled location 3")

    # event description | name="description"
    desc_box = driver.find_element(By.NAME, "description")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", desc_box)
    time.sleep(0.5)
    driver.execute_script("arguments[0].value = arguments[1];", desc_box, event_data['desc'])
    print("filled description")

    input("Press Enter here once you have submitted the form...")

    driver.quit()