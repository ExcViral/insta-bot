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
username.send_keys('your_username')
sleep(3)

# type in the password and press ENTER key
password = browser.find_element_by_name('password')
password.send_keys('your_password')
password.send_keys(Keys.ENTER)
sleep(3)

#comment these lines out, if you don't get a pop up asking about notifications after logging in
notnow = browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()


# ##########################################################
# ## FUNCTIONS #############################################
# ##########################################################


def follow_by_tags(hashtag_list, engagement_target):

    new_followed = []
    tag = -1
    followed = 0
    likes = 0

    for hashtag in hashtag_list:
        tag += 1
        browser.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
        sleep(5)
        first_thumbnail = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

        first_thumbnail.click()
        sleep(randint(1, 2))
        try:
            for x in range(1, engagement_target):
                username = browser.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text

                if username not in new_followed:
                    # If we already follow, do not unfollow
                    if browser.find_element_by_xpath(
                            '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                        browser.find_element_by_xpath(
                            '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                        new_followed.append(username)
                        followed += 1

                        # Liking the picture
                        button_like = browser.find_element_by_xpath(
                            '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')

                        button_like.click()
                        likes += 1
                        sleep(randint(18, 25))
                    # Next picture
                    browser.find_element_by_link_text('Next').click()
                    sleep(randint(25, 29))
                else:
                    browser.find_element_by_link_text('Next').click()
                    sleep(randint(20, 26))
        # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
        except:
            continue

    updated_user_df = pd.DataFrame(new_followed)
    updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
    print('Liked {} photos.'.format(likes))
    print('Followed {} new people.'.format(followed))


follow_by_tags(["marvel"], 10)