#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
from selenium import webdriver
from datetime import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# from pyvirtualdisplay import Display
#
# # initiate virtual display
# display = Display(visible=0, size=(1080, 920))
# display.start()


def loginToAccount(UsrName, Password):
    ## GOES TO INSTAGRAM LOGIN PAGE
    driver.get('https://www.instagram.com/accounts/login/')
    print (driver.title).encode('utf-8')

    ## ENTERS THE USERNAME AND PASSWORD
    user = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    user.send_keys(UsrName)
    time.sleep(1)
    passwordd = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    passwordd.send_keys(Password)
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    time.sleep(2)
    print (driver.title).encode('utf-8')
    print (driver.current_url)

    ## DELETE AFTER
    try:

        submit_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Send Security Code')]")))
        submit_button.click()
        time.sleep(10)
        codee = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='securityCode']")))
        codee.send_keys('894026')
        codee.send_keys(u'\ue007')
        time.sleep(20)

        driver.get('https://www.instagram.com/accounts/login/')
        print driver.title.encode('utf-8')

        ## ENTERS THE USERNAME AND PASSWORD
        user = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        user.send_keys(UsrName)
        time.sleep(1)
        passwordd = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        passwordd.send_keys(Password)
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
        time.sleep(2)
        print driver.title.encode('utf-8')
        print (driver.current_url)

    except:
        pass


def enterCelebrityAccountFollowers(url):
    ## GOES TO THE CELEBRITY ACCOUNT
    driver.get(url)

    ## ENTERS CELEBRITY ACCOUNT FOLLOWERS
    Followers_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
    Followers_button.click()


#     print (driver.title).encode('utf-8')

def getInsideSomeAccount(index):
    ## ENTERS THE ACCOUNT PROFILE AND WAITS FOR ALL PROFILES TO LOAD - THEN CLICKS ON PROFILE BY INDEX
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, '_6e4x5')))  ##ELEMENT NEEDS CHANGE* FINDS ALL LIST ITEMS
    Profile = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@class='_2g7d5 notranslate _o5iw8']")))[
        index]  ## ELEMENT NEEDS CHANGE

    Profile.click()


def waitUntilTimeReached(FirstTime, SecondTime, TimeDesiredToSleep):
    TimePassed = SecondTime - FirstTime
    SleepingTime = TimeDesiredToSleep - TimePassed

    if SleepingTime < 0:
        return 0

    else:
        return SleepingTime


def handleExceptionForFollow(FollowedUrList):
    driver.refresh()

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(.,'Following') or contains(.,'Requested')]")))

        FollowedUrList.append(driver.current_url)
        return FollowedUrList

    except Exception as e:
#         print e
        return FollowedUrList
        pass


def followActiveAccount():
    AmountOfActiveFollowed = 0
    AmountOfFectiveFollowed = 0
    now = time.time()
    index = 0
    FollowedUrList = []

    enterCelebrityAccountFollowers(celebrityAccountURL)
    getInsideSomeAccount(index)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CLASS_NAME, '_fd86t')))  ##ELEMENT NEEDS CHANGE* WAITS UNTIL THE AMOUNT POSTS ELEMENT IS AVAILABLE

    #     print ("Site At Profile: "),driver.title.encode('utf-8')
    time.sleep(2)

    for y in range(0, 12):

        print datetime.today()
        startHour = time.time()

        for x in range(0, 70):

            try:
                follow_button = driver.find_element_by_xpath(
                    "//button[contains(.,'Follow')]")  ## NO NEED TO CHANGE ELEMENT

                follow_button.click()

                WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(.,'Following') or contains(.,'Requested')]")))

                FollowedUrList.append(driver.current_url)

            except:
                FollowedUrList = handleExceptionForFollow(FollowedUrList)
                pass

            now = time.time()

            enterCelebrityAccountFollowers(celebrityAccountURL)
            index = 0

            while True:

                try:
                    getInsideSomeAccount(index)
                    time.sleep(2)
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                                   '_fd86t')))  ##ELEMENT NEEDS CHANGE* WAITS UNTIL THE AMOUNT POSTS ELEMENT IS AVAILABLE
                    #                     print ("Site At Profile: "),driver.title.encode('utf-8')

                    PostAmount = driver.find_element_by_class_name('_fd86t').text
                    #                     print ('Number Of Posts: '),PostAmount

                    follow_button1 = driver.find_elements_by_xpath(
                        "//button[contains(.,'Following')]")  ## NO NEED TO CHANGE ELEMENT
                    follow_button2 = driver.find_elements_by_xpath(
                        "//button[contains(.,'Requested')]")  ## NO NEED TO CHANGE ELEMENT

                    ## CHECKS IF ACCOUNT HAS NOT ALREADY BEEN FOLLOWED
                    if follow_button1.__len__() == 0 and follow_button2.__len__() == 0:

                        after = time.time()

                        if int(after) - int(now) > 45.5:  ##THERE IS A TIME.SLEEP FOR 2 SEC
                            AmountOfFectiveFollowed += 1
                            time.sleep(2)
                            #                             print ('Fictive Follow: '),AmountOfFectiveFollowed
                            break

                        ## CHECKS IF ACCOUNT HAS MORE THAN 40 POSTS - IF DOES, FOLLOWED
                        elif 40 <= int(PostAmount) < 200:
                            AmountOfActiveFollowed += 1

                            after = time.time()
                            LoadingTime = waitUntilTimeReached(now, after, 47)
                            time.sleep(LoadingTime)

                            #                             print ('Active Follow: '),AmountOfActiveFollowed

                            break

                    ## IF, ONE OF THE IF'S STATEMENTS ARE FALSE, DRIVER GOES BACK TO LIST TO TRY NEXT ACCOUNT
                    index += 1

                    ## AFTER 20 PROFILES, LIST INDEX WILL BE OUT OF RANGE, SO THIS WILL HANDLE
                    if index > 19:
                        index = 0
                        enterCelebrityAccountFollowers(celebrityAccountURL)

                    else:
                        driver.back()

                except Exception as e:
                    print (e)
                    enterCelebrityAccountFollowers(celebrityAccountURL)
                    index = 0

        endHour = time.time()

        LoadinggTimee = waitUntilTimeReached(startHour, endHour, 3600)
        time.sleep(LoadinggTimee)

    print ("TODAY PROGRAM FOLLOWED: "), FollowedUrList.__len__()
    return FollowedUrList


def Unfollow(FollowedUrList):
    Unfollowed = 0
    fucked = 0
    Starthour = time.time()
    now = time.time()
    counterforwait = 0

    for url in FollowedUrList:
        try:
            driver.get(url)

            after = time.time()

            LoadingTime = waitUntilTimeReached(now, after, 47)

            time.sleep(LoadingTime)

            try:
                print "Account: ", driver.title.encode('utf-8')

            except Exception as e:
                print (e)
                pass

            try:
                Unfollow_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(.,'Following') or contains(.,'Requested')]")))
                Unfollow_button.click()

            except Exception as e:
                print (e), "Cant Find Unfollow"
                fucked += 1
                # handleExceptionEnteringAccount()

            if Unfollowed % 70 == 0 and Unfollowed != 0:
                counterforwait += 1
                TimeTowait = 3600 * counterforwait
                EndHour = time.time()
                LoadinggTimme = waitUntilTimeReached(Starthour, EndHour, TimeTowait)
                time.sleep(LoadinggTimme)
                print datetime.today()

            now = time.time()

            try:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(.,'Follow')]")))

                time.sleep(1)

                Unfollowed += 1

            except Exception as e:
                print (e), "Cant Find Follow After Unfollow"
                # Unfollowed = handleExceptionAfterClick(Unfollowed)
                fucked += 1


                # print ('Unfollowed '),Unfollowed,('accounts')

        except Exception as e:
            print (e)
            pass

    print ('UNFOLLOWED ACCOUNTS FOR TODAY:'), Unfollowed
    print "NUMBER OF FUCKED ACCOUNTS:", fucked


def handleExceptionEnteringAccount():
    driver.refresh()
    time.sleep(5)
    try:
        Unfollow_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(.,'Following') or contains(.,'Requested')]")))

        Unfollow_button.click()

    except:
        print ('following or requested button from profile account not found')
        pass


def handleExceptionAfterClick(Unfollowed):
    driver.refresh()
    time.sleep(5)

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(.,'Follow')]")))

        Unfollowed += 1
        return Unfollowed

    except:
        print ('follow button after unfollow not found')
        return Unfollowed


username = 'puberty_goals.09'
password = '158123RA'
celebrityAccountURL = 'https://www.instagram.com/9gag/'

GOOGLE_CHROME_BIN = r"/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = r"/app/.chromedriver/bin/chromedriver"

chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

driver.maximize_window()

loginToAccount(username, password)

while True:
    noww = time.time()

    Followed = followActiveAccount()
    Unfollow(Followed)

    ## checks if 24 hours had passed - if not, waits until 24H and 2 minutes will pass
    afterr = time.time()
    LoadinggTime = waitUntilTimeReached(noww, afterr, 86520)  
    time.sleep(LoadinggTime)

    print 'PROGRAM FINISHED FOR TODAY', datetime.today()
    break
