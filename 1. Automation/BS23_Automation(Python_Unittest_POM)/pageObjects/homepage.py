class HomePage():

    # locators of all the elements:

    homepage_url = "http://automationpractice.com/index.php"
    hp_signin_PlinkText = "Sign"

    # default Constructor
    def __init__(self,driver):
        self.driver = driver
        
    #page actions
    def login_Click(self):
        self.driver.find_element_by_partial_link_text(self.hp_signin_PlinkText).click()
