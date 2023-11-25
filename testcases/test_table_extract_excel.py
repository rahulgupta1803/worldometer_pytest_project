import time

from selenium.webdriver.common.by import By

from pageobjects.worldometer_page import World_Meter
from utilities import xlutils


class Test_World_meter():
    excel_path = "D:\\credence\\worldometer_pytest_project\\testcases\\testdata\\extract_table.xlsx"

    def test_world_meter(self, setup):
        self.driver = setup
        self.wmp = World_Meter(self.driver)
        time.sleep(3)
        self.wmp.Scroll_Page()
        time.sleep(3)
        print(f" column length: {self.wmp.Column_Length()}")
        print(f"row length: {self.wmp.Row_Length()}")
        cl=self.wmp.Column_Length()
        rl=self.wmp.Row_Length()
        for r in range(1,cl):
            xlutils.WriteData(self.excel_path,"Sheet1",1,r,self.wmp.Header(r))
            for x in range(1,rl):
                time.sleep(1)
                self.wmp.Iterating(r,x)
                xlutils.WriteData(self.excel_path,"Sheet1",x+1,r,self.wmp.Iterating(r,x))
        print("Extraction is complete")











# pytest -v -s --browser chrome "D:\credence\worldometer_pytest_project\testcases\test_table_extract_excel.py"
