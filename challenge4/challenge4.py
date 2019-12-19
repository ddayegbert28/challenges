import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Challenge4(unittest.TestCase):

    def before(newWebsite):
        self.driver = webdriver.Chrome("../chromedriver")
        driver = self.driver
        """ goto website """
        driver.get(newWebsite)

    def setUp(self):
        before("https://www.copart.com");

    def tearDown(self):
        self.driver.close()

    def test_popular_in_copart_forLoop(self):
        self.assertIn("Copart", self.driver.title)
        """ Check that the Most Popular Items in the page """
        self.assertIn("Most Popular Items", self.driver.page_source)



if __name__ == '__main__':
    unittest.main()