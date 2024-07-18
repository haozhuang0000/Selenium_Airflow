from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

_ = load_dotenv(find_dotenv())

def get_driver():
    options = Options()
    options.set_capability('se:recordVideo', True)
    options.set_capability('se:screenResolution', '1920x1080')
    options.set_capability('se:name', 'test_visit_basic_auth_secured_page (ChromeTests)')
    driver = webdriver.Remote('http://selenium-hub-tutorial:4444', options=options)
    return driver