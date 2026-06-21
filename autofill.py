# ==== selenium -- autofilling on the web ====
# launch and control browser window 
from selenium import webdriver 
# locating elements on page to fill input boxes 
from selenium.webdriver.common.by import By 
# handles dropdown menus (room choices), wait until item loads before interact 
from selenium.webdriver.support.ui import Select, WebDriverWait 
# ExpCond + WebDriverWait => until element visible/clickable 
from selenium.webdriver.support import expected_conditions as ExpCond

# for CHROME 
# from webdriver_manager.chrome import ChromeDriverManager 
# from selenium.webdriver.chrome.service import Service 

# for SAFARI
# Safari > Settings > Advanced > "show features for web developers" 
# Safari > Settings > Developer > "Allow Remote Automation "
driver = webdriver.Safari  