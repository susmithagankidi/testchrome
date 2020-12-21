from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome(executable_path=binary_path,chrome_options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
