from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(executable_path = "C:\Users\HP\Documents\pythonbasic\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


