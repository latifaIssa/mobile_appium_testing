import requests

from appium import webdriver
from selenium.webdriver.common.by import By
# # pip install eyes-selenium to install the sdk
from applitools.selenium.eyes import Eyes

# Desired capabilities
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11.0",
    # Write adb devices in bash to show the device name: 5c2f76be
    'deviceName': '5c2f76be',
    "browserName": "chrome",
    # 'automationName': 'UIAutomator2',
    "autoGrantPermissions": "true",
    'autoAcceptAlerts': 'true',
    'goog:chromeOptions': {
        'w3c': True
    }

    # This command line for app testing
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
    driver.implicitly_wait(20)
    driver.find_element(By.CSS_SELECTOR, '#elements > button').click()
    driver.implicitly_wait(10)
    driver.back()

    # find broken images
    driver.find_element(By.XPATH, '//a[@href="/broken_images" and (text()="Broken Images")]').click()
    driver.implicitly_wait(10)
    images = driver.find_elements(By.XPATH, '//div[@class="example"]/img')
    for i in images:
        r = i.size['width']
        s = i.get_attribute('src')
        # if i != '':
        #     assert r != '0'
        req = requests.get('https://the-internet.herokuapp.com/'+s)
        if req.status_code != 200:
            print(f"this image {i} is broken")

    driver.back()
