from selenium.webdriver.common.by import By


class World_Meter():
    scroll_element_XPATH = (By.XPATH, '//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[2]')
    row_length_XPATH = (By.XPATH,'//*[@id="main_table_countries_today"]/tbody[1]/tr/td[1]')
    column_length_XPATH = (By.XPATH,'//*[@id="main_table_countries_today"]/tbody[1]/tr[1]/td')

    def __init__(self, driver):
        self.driver = driver

    def Scroll_Page(self):
        m = self.driver.find_element(*World_Meter.scroll_element_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", m)

    def Row_Length(self):
        row_length = len(self.driver.find_elements(*World_Meter.row_length_XPATH))
        return row_length

    def Column_Length(self):
        col_length = len(self.driver.find_elements(*World_Meter.column_length_XPATH))
        return col_length

    def Iterating(self,a,b):
        n = self.driver.find_element(By.XPATH,'//*[@id="main_table_countries_today"]/tbody[1]/tr['+str(b)+']/td['+str(a)+']').text
        return n

    def Header(self,d):
        c = self.driver.find_element(By.XPATH,'//*[@id="main_table_countries_today"]/thead/tr/th['+str(d)+']').text
        return c




