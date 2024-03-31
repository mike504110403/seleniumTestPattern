from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from BeautifulReport import BeautifulReport
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

'''
擊滑鼠右鍵: context_click()
雙擊滑鼠左鍵: double_click()
按著滑鼠左鍵不放: click_and_hold()
放開滑鼠左鍵: release()
拖曳到某個元素後放開: drag_and_drop(source, target)
拖曳到某個座標後放開: drag_and_drop_by_offset(source, xoffset, yoffset)
按下鍵盤上某個按鍵: key_down(value)
放開鍵盤上某個按鍵: key_up(value)
滑鼠指標從當前位置移動到某個座標: move_by_offset(xoffset, yoffset)
滑鼠指標移動到某個元素: move_to_element(to_element)
移動到某元素附近座標位置: move_to_element_with_offset(to_element, xoffset, yoffset)
執行當前這個ActionChain的動作: perform()
在元素上輸入值(ex:input): send_keys(value)
在指定的元素上輸入值: send_keys_to_element(element, value)
'''

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
    "profile.password_manager_enabled": False,
    "credentials_enable_service": False
})
                                
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(options=options)
        print("WebDriver 初始化成功:", self.driver)
        self.action = ActionChains(self.driver)
        self.URL = "https://youtube.com"
        self.driver.get(self.URL)
        self.driver.maximize_window()
    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        
    def test_01_search(self):
        """
        前往Youtube網站後，搜尋Gura的影片
        """
        time.sleep(5)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))
            )
        finally:
            print("找不到")
            time.sleep(5)

        input_search = self.driver.find_element_by_xpath("//input[@id='search']")
        time.sleep(5)
        input_search.send_keys("Gawr Gura 熟肉")
        time.sleep(5)
        button_search = self.driver.find_element_by_xpath("//button[@id='search-icon-legacy']")
        time.sleep(5)
        button_search.click()
    
    def test_02_open_target(self):
        """
        在搜尋結果找到特定的影片並點進去
        """
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,1200)")
        time.sleep(5)
        
        youtube_target = self.driver.find_element_by_xpath("//a[@href='/watch?v=9SfsF_6fY9c']")
        youtube_target.click()
        time.sleep(5)
        
    def test_03_back_to_list(self):
        """
        回上頁列表，重新整理網頁後，切換另一則影片，五秒後回到首頁
        """
        self.driver.back()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)
        youtube_target = self.driver.find_element_by_xpath("//a[@href='/watch?v=MhVh01k_Wg0']")
        youtube_target.click()
        time.sleep(5)
        logo = self.driver.find_element_by_id("logo-icon")
        logo.click()
        time.sleep(5)

basedir = "D:/auto_test/"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(basedir, pattern='*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='report',description='我的第一個測試', log_path='D:/auto_test/')
