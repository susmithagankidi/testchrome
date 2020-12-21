from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary  # Adds chromedriver binary to path

options = Options()
options.add_argument("--headless") #open Browser in maximized mode
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("disable-extensions")
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
driver = webdriver.Chrome(executable_path=binary_path,chrome_options=chrome_options)
# executable_path=binary_path,
driver.get("http://www.python.org")
assert "Python" in driver.title
