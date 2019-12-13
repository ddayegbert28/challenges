import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        driver=self.driver
        """ goto website """
        driver.get("https://www.copart.com")
        """ check the title """

    def tearDown(self):
        self.driver.close()

    def test_popular_in_copart_forLoop(self):
        self.assertIn("Copart", self.driver.title)
        """ Check that the Most Popular Items in the page """
        self.assertIn("Most Popular Items", self.driver.page_source)
        """ Find and print a list of the Most Popular elements using a XPATH """
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        for x in elements:
            print (x.text + " - " + x.get_attribute("href"))

    def test_popular_in_copart_whileLoop(self):
        self.assertIn("Copart", self.driver.title)
        """ Check that the Most Popular Items in the page """
        self.assertIn("Most Popular Items", self.driver.page_source)
        """ Find and print a list of the Most Popular elements using a XPATH """
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        numElems = len(elements)
        i = 0
        while i < numElems:
            print (elements[i].text + " - " + elements[i].get_attribute("href"))
            i += 1


        """ FYI...How to get all the attributes of an element """
        # logo = driver.find_element(By.XPATH, "//*[@id=\"channelList\"]//img")
        # attrs=[]
        # for attr in logo.get_property('attributes'):
        #     attrs.append([attr['name'], attr['value']])
        # print(attrs)


if __name__ == '__main__':
    unittest.main()