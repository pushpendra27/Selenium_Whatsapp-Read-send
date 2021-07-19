import os
import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import pickle
import shutil
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


# Function for getting user from
def new_chat(user_name):
    # Selecting the new chat search textbox
    new_chat = driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"]') #Div Class
    # //span[@data-testid='search']
    # //button[@class='_1Ek-U']
    new_chat.click()
    print(" Selecting New Chat, Done")

    # Enter the name of chat
    new_user = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    new_chat.send_keys(user_name)
    print("Name Has Been Selected")
    time.sleep(1)


    time.sleep(1)

    try:
        # Select for the title having user name
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        # Close the browser
        driver.close()
        print(e)
        sys.exit()

"""    try:
        # Select for the title having user name
        #user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user = driver.find_element_by_xpath('//div[contains(text(),"{}")]'.format(user_name))

        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        # Close the browser
        driver.close()
        print(e)
        sys.exit()"""

if __name__ == '__main__':

    browser_name = "chrome"

    if browser_name == "chrome":

        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
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
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        #`      user_agent=driver.execute_script("return navigator.userAgent;")
        driver.implicitly_wait(5)
    elif browser_name == "firefox":

        options = webdriver.FirefoxOptions()
        #options.headless = True

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        currentProfilePath = driver.capabilities["moz:profile"]
        print("CurrentProfilePath:",currentProfilePath)
        profileStoragePath = "/tmp/abc"

        """
        cookies = pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
        cookies = pickle.load(open("cookies.pkl","rb"))
        driver.add_cookie(cookies)
        """

        shutil.copytree(currentProfilePath, profileStoragePath,ignore_dangling_symlinks=True)
        driver = webdriver(executable_path="/home/pushpendra/.wdm/drivers/geckodriver/linux64/v0.29.1",firefox_profile=FirefoxProfile(profileStoragePath))


    else:
        print("_____Please Enter Correct Browser Name Before Move Further____"+browser_name)



    # Register the drive
    driver.get('https://web.whatsapp.com/')
    print(driver.title)
    time.sleep(10)
    driver.get_screenshot_as_file(os.getcwd() + "/screenshots/"+"WhatsappPageChromeError" + ".png")

    # Sleep to scan the QR Code
    time.sleep(5)

    user_name_list = ["Cofybiz FB TG","My reliance"]
    user_message_list= 'Hey, Successfully Running Your Bots for Whatsapp Messages'

    for user_name in user_name_list:

        try:
            # Select for the title having user name
            #user = driver.find_element_by_xpath("//input[@title='Search or start new chat']").send_keys(user_name)
            user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
            print("______Entered Done______")
            driver.get_screenshot_as_file(os.getcwd() + "/screenshots/" + "Selenium_" + user_name +".png")
            #input("Enter for Mesage imput") #For Testing Purpose Input Enter

        except NoSuchElementException as se:
            new_chat(user_name)

        # Typing message into message box
        #message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(user_message_list)
        #message_box=driver.find_element_by_xpath('//span[@title="{}"]'.format(user_message_list))
        #message_box.send_keys(Keys.ENTER)


        message_box = driver.find_element_by_xpath('//div[@class="_2A8P4"]')
        message_box.send_keys('{}'.format(user_message_list)+Keys.ENTER)
        driver.get_screenshot_as_file(os.getcwd() + "/screenshots/" + "Selenium_1" + user_name + ".png")
        time.sleep(3)

    #input("Enter for Browser")
    driver.close()
    driver.quit()