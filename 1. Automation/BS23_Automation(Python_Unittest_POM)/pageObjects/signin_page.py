
class SigninPage():

    # locators of all the elements:

    sp_email_css = "#email"
    sp_password_css = "#passwd"
    sp_login_btn_css = "body.authentication.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div.row div.col-xs-12.col-sm-6:nth-child(2) form.box div.form_content.clearfix p.submit:nth-child(4) button.button.btn.btn-default.button-medium > span:nth-child(1)"
    sp_create_ac_email_xpath = "//input[@id='email_create']"
    sp_create_ac_btn_css = "body.authentication.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div.row div.col-xs-12.col-sm-6:nth-child(1) form.box div.form_content.clearfix div.submit:nth-child(4) button.btn.btn-default.button.button-medium.exclusive:nth-child(2) > span:nth-child(1)"

    #default Constructor
    def __init__(self,driver):
        self.driver = driver

    #page actions
    def setNewEmail(self,email):
        self.driver.find_element_by_xpath(self.sp_create_ac_email_xpath).send_keys(email)

    def ClickEmailCheck(self):
        self.driver.find_element_by_css_selector(self.sp_create_ac_btn_css).click()

    def setEmail(self,email):
        self.driver.find_element_by_css_selector(self.sp_email_css).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_css_selector(self.sp_password_css).send_keys(password)

    def loginClick(self):
        self.driver.find_element_by_css_selector(self.sp_login_btn_css).click()