# ##########################################################
# ## IMPORT LIBRARIES ######################################
# ##########################################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import re


# ##########################################################
# ## SETUP #################################################
# ##########################################################

# specify the webdriver
# edit the chromedriver address according to your file system
chromedriver_path = "/home/excviral/JupyterProjects/insta-bot/chromedriver"
browser = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

# open a new window and open login page of instagram
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

# type in the username
username = browser.find_element_by_name('username')
username.send_keys('your_username_here')
sleep(3)

# type in the password and press ENTER key
password = browser.find_element_by_name('password')
password.send_keys('your_password_here')
password.send_keys(Keys.ENTER)
sleep(3)

#comment these lines out, if you don't get a pop up asking about notifications after logging in
notnow = browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()


# ##########################################################
# ## FUNCTIONS #############################################
# ##########################################################
