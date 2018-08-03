import time
from selenium import webdriver


class webcontrol(object):

    def __init__(self,browser = 'Chrome'):
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()

    def play_music(self, what = 'ACDC'):
        self.driver.get('http://youtube.com')
        elm = self.driver.find_element_by_name('search_query').send_keys(what)
        self.driver.find_element_by_id('search-icon-legacy').click()
        
        elm = self.driver.find_element_by_id('dismissable').click()     
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