import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_search_in_copart(self):
        driver=self.driver
        """ goto website """
        driver.get("https://www.copart.com")
        """ check the title """
        self.assertIn("Copart", self.driver.title)
        """ Find the search """
        elem = driver.find_element_by_id("input-search")
        """ Enter a search phrase """
        elem.send_keys("exotics")
        elem.send_keys(Keys.RETURN)
        """ check that some results are found """
        assert "porsche" not in driver.page_source


if __name__ == '__main__':
    unittest.main()