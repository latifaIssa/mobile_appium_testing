from appium import webdriver
from selenium.webdriver.common.by import By
# # pip install eyes-selenium to install the sdk
# from applitools.selenium.eyes import Eyes

# Desired capabilities
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11.0",
    # Write adb devices in bash to show the device name
    "deviceName": "OPPO A9 2020",
    "browserName": "Chrome",
    'automationName': 'UIAutomator2',
    "autoGrantPermissions": "true",
    'autoAcceptAlerts': 'true',
    'goog:chromeOptions': {
        'w3c': False
    }

    # This command line for app tesitng
    # to find out app package: adb shell dumpsys window | find "mCurrentFocus"
}

class FirstTest:
    # Create driver instance
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(30)

    # Navigate the browser to the "Internet" web-site.
    driver.get(r'https://the-internet.herokuapp.com/')

    # Click on A/B Testing
    driver.find_element(By.XPATH, '//a[@href="/abtest" and (text()="A/B Testing")]').click()
    driver.implicitly_wait(10)
    driver.back()

    # Add/Remove Elements
    driver.find_element(By.XPATH, '//a[@href="/add_remove_elements/" and (text()="Add/Remove Elements")]').click()
    driver.implicitly_wait(10)
    driver.find_element(By.TAG_NAME, 'button').click()
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, 'added-manually').click()
    driver.implicitly_wait(10)
    driver.back()

    # find broken images
    images = driver.find_elements(By.TAG_NAME, 'img')
    for i in images:
        if(i != ''):
            assert i.get_attribute('natural_size') == '0'

    driver.back()












