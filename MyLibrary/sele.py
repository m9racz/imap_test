import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class webcontrol(object):

    def __init__(self,browser = 'Chrome'):
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()

    def play_music(self, what = 'ACDC'):
        self.driver.get('http://youtube.com')
        elm = self.driver.find_element_by_name('search_query').send_keys(what)
        self.driver.find_element_by_id('search-icon-legacy').click()
        time.sleep(3)
        #elm = self.driver.find_element_by_id('dismissable').click()     
        elm = self.driver.find_element_by_xpath("//div[@id='contents']//ytd-video-renderer[2]//div[@id='dismissable']//ytd-thumbnail[1]//a[@id='thumbnail']").click()
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='contents']//ytd-video-renderer[2]//div[@id='dismissable']//ytd-thumbnail[1]//a[@id='thumbnail']"))).click()
        #ytd-playlist-renderer
        #ytd-video-renderer
        #ytd-channel-renderer             


        #print (elm)
        #//*[@id="fox"]/a
        #to find the link in the 2nd div with class ‘abc’:
        #(//div[@class='abc'])[2]/a
        #print(elm)
        #elm.click()
        #time.sleep(10)
        #self.driver.quit()
   

'''
driver = webdriver.Chrome()
driver.get('http://google.com')
elm = driver.find_element_by_name('btnI')
elm.click()
print(driver.current_url)
time.sleep(15)
driver.quit()
'''