from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import getpass
from time import sleep
class TinderBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # prefs = {
        #     "profile.managed_default_content_settings.images": 2
        # }
        # chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            './chromedriver', chrome_options=chrome_options)

    
    def login(self):
        self.driver.get('https://tinder.com')
        sleep(5)

        fb_btn_login = self.driver.find_element_by_css_selector(
            'button[aria-label="Log in with Facebook"]')
        fb_btn_login.click()

        #swith to login popup
        base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_ip=self.driver.find_element_by_css_selector('#email')
        email_ip.send_keys('nghiahsgs')

        pass_ip = self.driver.find_element_by_css_selector('#pass')
        pw=getpass.getpass(prompt='Password: ')
        pass_ip.send_keys(pw)
        
        
        login_btn = self.driver.find_element_by_css_selector(
            'input[name="login"]')
        login_btn.click()

        #swith to base windonw
        self.driver.switch_to_window(base_window)
        sleep(5)

        btn_allow = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="allow"]')))
        btn_allow.click()
        btn_allow = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="allow"]')))
        btn_allow.click()

       
        
        sleep(2)

    def keep_swiping(self):
        btn_keep_swiping = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        btn_keep_swiping.click()

    def auto_like(self):
        while(True):
            try:
                self.like()
            except Exception:
                try:
                    self.keep_swiping()
                except Exception:
                    try:
                        self.ignoreInterested()
                    except Exception:
                        pass
            sleep(1)
    def ignoreInterested(self):
        btn_not_interested = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        btn_not_interested.click()

    def like(self):
        btn_like = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        btn_like.click()

    def disLike(self):
        btn_dislike = self.driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        btn_dislike.click()


bot = TinderBot()
bot.login()
bot.auto_like()
