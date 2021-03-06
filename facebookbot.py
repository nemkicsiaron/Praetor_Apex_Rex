from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

botlist = json.load(open('bots.json',))

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

class FaceBot:
    def __init__(self, email, pw):
        super().__init__()
        self.driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')
        self.driver.get("https://facebook.com")
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]")\
            .click()
        self.driver.find_element_by_xpath("//input[@name=\"email\"]")\
            .send_keys(email)
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("//button[@name=\"login\"]")\
            .click()

    def profile(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div/div[1]/img")\
            .click()
        self.driver.find_element_by_xpath("//*[@id=\"mount_0_0\"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]")\
            .click()

for i in botlist:
    if( i["id"][2 : 4] == "FB" ):
        bot = FaceBot( i["email"], i["password"] )
        sleep(4)
        bot.profile()