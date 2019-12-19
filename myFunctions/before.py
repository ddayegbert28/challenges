def before (newWebsite):
    self.driver = webdriver.Chrome("../chromedriver")
    driver=self.driver
    """ goto website """
    driver.get(newWebsite)

