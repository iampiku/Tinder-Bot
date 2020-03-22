from selenium import webdriver
from time import sleep

# We are importing the email id and password for privacy !
from user_credentials import user_email_id, password


class Tinder_Bot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):

        self.driver.maximize_window()
        self.driver.get('https://tinder.com')

        sleep(3)   # We pause for the login pop up to show up 

        tinder_win = self.driver.window_handles[0]  # Before clicking on the option(Login with facebook) store the window

        # In selenium automation if the element are not found by general locator then XPath is used to find the element in html
        facebook_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        facebook_button.click()

        # We will be switching to facebook login window
        facebook_login = self.driver.window_handles[1]

        self.driver.switch_to_window(facebook_login)

        # filling up login fields in facebook login pop up
        email_id = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_id.send_keys(user_email_id)
        email_pass = self.driver.find_element_by_xpath('//*[@id="pass"]')
        email_pass.send_keys(password)

        log_in = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        log_in.click()

        self.driver.switch_to_window(tinder_win)

        sleep(15) # screen load time

        location_pop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        location_pop.click() 

        enable_pop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable_pop.click() # enable location request 

        sleep(6) # screen load time

    def right_swipe(self): # fuction to click on the right swipe button   
        like_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    def left_swipe(self): # fuction to click on the left swipe button
        cross_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        cross_button.click()

    def message_pop(self): # fuction to avoid unnecessary message pop ups
        message = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        message.click()
    
    def match_close(self): # fuction to avoid unnecessary match notification pop ups
        match = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match.click()

    def auto_swipe(self): # auto swipe fuction 
        while True:
            sleep(1.5)
            try:
                self.right_swipe()
            except Exception:
                try:
                    self.message_pop()
                except Exception:
                    self.match_close()


obj = Tinder_Bot() # creating object of the class
obj.login()
obj.auto_swipe()



        
















