from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
caps = chrome_options.to_capabilities()

#options = wd.ChromeOptions()
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#caps = options.to_capabilities()
#driver = wd.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
#                            desired_capabilities=caps)

#This is the Chrome webdriver's filepath
driver = wd.Chrome(executable_path='/Users/reidbrown/PycharmProjects/2019_AllStar_Voting/chromedriver', desired_capabilities=caps)

#NBA fan voting URL that the Driver opens
driver.get('https://www.google.com/search?q=nba+vote&oq=nba+vote&aqs=chrome.0.69i59j69i57j69i60l4.986j0j1&sourceid=chrome&ie=UTF-8')

#Clicks Hornets
driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div/g-scrolling-carousel/div[1]/div/div[1]/g-inner-card[4]/div').click()

#Clicks Devonte' Graham
driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[5]/g-scrolling-carousel/div[1]/div/div[1]/g-inner-card[5]/div/div[2]/div/div[1]/div[1]/div').click()

#Click "Sign into Vote"
driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[4]/div/div[1]/div[1]/g-raised-button/div').click()

#Send email to email textbox
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('my_email')

time.sleep(1)
#Click Next
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span').click()

time.sleep(1)
#Send password to textbox
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys('my_password')

time.sleep(1)
#Click Next
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span').click()
