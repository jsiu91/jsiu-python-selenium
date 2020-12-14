#!/usr/bin/env python3

import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./drivers/chromedriver")
        self.driver.get("https://www.python.org")
    
    #any test method needs to start with word "test"
    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
