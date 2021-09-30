from selenium import webdriver
from selenium.webdriver.support.ui import Select
class RegisterPage():

     # locators of all the elements:
     rp_gender_css = "#id_gender1"
     rp_fname_css = "#customer_firstname"
     rp_lname_css = "#customer_lastname"
     rp_password_css = "#passwd"
     rp_dob_day_css = "#days"
     rp_dob_month_css = "#months"
     rp_dob_year_css = "#years"
     rp_address_css = "#address1"
     rp_city_css ="#city"
     rp_state_css= "#id_state"
     rp_postcode_css = "#postcode"
     rp_contry_css = "#id_state"
     rp_mobile_css = "#phone_mobile"
     rp_alias_css = "#alias"
     rp_registerBtn_css = "body.authentication.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div:nth-child(1) form.std.box div.submit.clearfix:nth-child(4) button.btn.btn-default.button.button-medium:nth-child(4) > span:nth-child(1)"

     # default Constructor
     def __init__(self, driver):
         self.driver = driver

     # page actions
     def setGender(self):
         self.driver.find_element_by_css_selector(self.rp_gender_css).click()

     def setFname(self,fname):
         self.driver.find_element_by_css_selector(self.rp_fname_css).send_keys(fname)

     def setLname(self,lname):
         self.driver.find_element_by_css_selector(self.rp_lname_css).send_keys(lname)

     def setPassword(self,password):
         self.driver.find_element_by_css_selector(self.rp_password_css).send_keys(password)

     def setDob_days(self,date):
         day = Select(self.driver.find_element_by_css_selector(self.rp_dob_day_css))
         day.select_by_value(date)


     def setDob_Months(self,mon):
         months = Select(self.driver.find_element_by_css_selector(self.rp_dob_month_css))
         months.select_by_value(mon)

     def setDob_years(self,year):
         years = Select(self.driver.find_element_by_css_selector(self.rp_dob_year_css))
         years.select_by_value(year)

     def setAddress(self,address):
         self.driver.find_element_by_css_selector(self.rp_address_css).send_keys(address)

     def setCity(self,city):
         self.driver.find_element_by_css_selector(self.rp_city_css).send_keys(city)

     def setState(self,state):
         states = Select(self.driver.find_element_by_css_selector(self.rp_state_css))
         states.select_by_value(state)

     def setPostcode(self,pcode):
         self.driver.find_element_by_css_selector(self.rp_postcode_css).send_keys(pcode)

     def setCountry(self,contry):
         contrys = Select (self.driver.find_element_by_css_selector(self.rp_contry_css))
         contrys.select_by_value(contry)

     def setMobile(self,mobile):
         self.driver.find_element_by_css_selector(self.rp_mobile_css).send_keys(mobile)

     def setAlias(self,alias):
         self.driver.find_element_by_css_selector(self.rp_alias_css).send_keys(alias)

     def setRegisterBtn(self):
         self.driver.find_element_by_css_selector(self.rp_registerBtn_css).click()
