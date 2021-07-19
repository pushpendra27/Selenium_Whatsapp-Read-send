import os
import sys
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
import shutil
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


if __name__ == '__main__':

    browser_name = "chrome"

    if browser_name == "chrome":

        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        """opt = Options()
          opt.add_argument("--headless")
          options.headless = True
          driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
          driver=webdriver.Chrome()"""

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument('--user-data-dir=</home/pushpendra/.config/google-chrome/default>')
        options.add_argument('--profile-directory=Default')
        #driver = webdriver.Chrome(chrome_options=options)
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        # `      user_agent=driver.execute_script("return navigator.userAgent;")
        driver.implicitly_wait(5)
    elif browser_name == "firefox":

        options = webdriver.FirefoxOptions()
        # options.headless = True

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        currentProfilePath = driver.capabilities["moz:profile"]
        print("CurrentProfilePath:", currentProfilePath)
        profileStoragePath = "/tmp/abc"

        shutil.copytree(currentProfilePath, profileStoragePath, ignore_dangling_symlinks=True)
        driver = webdriver(executable_path="/home/pushpendra/.wdm/drivers/geckodriver/linux64/v0.29.1",
                           firefox_profile=FirefoxProfile(profileStoragePath))

    else:
        print("_____Please Enter Correct Browser Name Before Move Further____" + browser_name)
    # Register the drive
    driver.get('https://web.whatsapp.com/')
    print(driver.title)
    #driver.get_screenshot_as_file(os.getcwd() + "/screenshots/" + "WhatsappPageChromeError" + ".png")
    # Sleep to scan the QR Code
    time.sleep(10)
    user_name_list = ["Rahul Deshmukh Sir","My reliance","Cofybiz FB TG","Prasad Dixit sir"]

    for user_name in user_name_list:

        try:
            # Select for the title having user name
            user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
            print("User Name  is selected:-", user.text)
            # ID Access
            time.sleep(10)
            #region = driver.find_elements_by_xpath('//div[@class="copyable-text"]')
            region=driver.find_elements_by_xpath("//div[@class[substring(.,string-length(.)-string-length('copyable-text')+1)='copyable-text']]")
            temp_len=len(region)
            print("Loading Last Ten Messages of Selected User.......\n")
            if len(region)<=10:
                length_msg=0
                temp_len=0
            else:
                length_msg=10 #For Desire Message length
                temp_len=len(region)
            region = driver.find_elements_by_xpath("//div[@class[substring(.,string-length(.)-string-length('copyable-text')+1)='copyable-text']]")[temp_len-length_msg:]
            #print(len(region))
            for container in region:
                print(container.get_attribute('data-pre-plain-text'),container.text)

        except NoSuchElementException as se:
            print("Something Error occured Try Again!!!")

    print("Thanks for Using Messages Reading of Whatsapp ")
    driver.close()
    driver.quit()

