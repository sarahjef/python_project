from datetime import time


def find_username(
        self):  # finds the username in the case of the program user is entered an e-mail adress instead of the username as a login info
    driver = self.driver
    self._username = driver.find_element_by_xpath("//a[@class='gmFkV']").text


class Keys(object):
    pass


def find_followings( driver, buttons):  # this functions finds the accounts who are followed by us

    # who do we follow
    following_button = [button for button in buttons if 'following' in button.get_attribute('href')]
    following_button[0].click()
    time.sleep(2)
    following_window = driver.find_element_by_xpath("//div[@role='dialog']//a")
    following_number = driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
    counter = 0
    while counter < int(
            following_number) / 5:  # scrolls 5 account each time approximately, if in your browser it differs, change the value with the passed account per scrolling
        following_window.send_keys(Keys.PAGE_DOWN)
        counter = counter + 1
        time.sleep(0.2)
    following_accounts = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate zsYNt ']")
    following_accounts = [account.get_attribute('title') for account in
                               following_accounts]  # the array of the accounts who we follow
    driver.find_element_by_xpath(
        "//span[@class='glyphsSpriteX__outline__24__grey_9 u-__7']").click()  # closes the following window


def find_followers(driver, buttons):  # this functions finds the accounts who are following us
    # who follows us
    follower_button = [button for button in buttons if 'followers' in button.get_attribute('href')]
    follower_button[0].click()
    time.sleep(2)
    follower_window = driver.find_element_by_xpath("//div[@role='dialog']//a")
    follower_number = driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
    counter = 0
    while counter < int(
            follower_number) / 5:  # scrolls 5 account each time approximately, if in your browser it differs, change the value with the passed account per scrolling
        follower_window.send_keys(Keys.PAGE_DOWN)
        counter = counter + 1
        time.sleep(0.2)
    follower_accounts = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate zsYNt ']")
    follower_accounts = [account.get_attribute('title') for account in
                              follower_accounts]  # the array of the accounts who follows us
    driver.find_element_by_xpath(
        "//span[@class='glyphsSpriteX__outline__24__grey_9 u-__7']").click()  # closes the follower window


