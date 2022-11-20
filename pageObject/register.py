import testData.registerData


class Register:

    def __init__(self, driver):
        self.driver = driver

    def registration(self):
        self.driver.find_element("xpath", "//a[@class = 'ico-register']").click()

    def gender(self):
        self.driver.find_element("xpath", "//input[@id='gender-male']").click()

    def name(self):
        # imported from testdata file
        self.driver.find_element("id", "FirstName").send_keys(testData.registerData.firstName)
        self.driver.find_element("id", "LastName").send_keys(testData.registerData.lastName)

    def dob(self):
        # imported from testdata file
        self.driver.find_element("name", "DateOfBirthDay").send_keys(testData.registerData.date)
        self.driver.find_element("name", "DateOfBirthMonth").send_keys(testData.registerData.month)
        self.driver.find_element("name", "DateOfBirthYear").send_keys(testData.registerData.year)

    def email(self):
        self.driver.find_element("id", "Email").send_keys(testData.registerData.email)

    def company(self):
        self.driver.find_element("id", "Company").send_keys(testData.registerData.company)

    def password(self):
        self.driver.find_element("id", "Password").send_keys(testData.registerData.password)

    def Confirmpass(self):
        self.driver.find_element("id", "ConfirmPassword").send_keys(testData.registerData.password)

    def RegConfirm(self):
        self.driver.find_element("xpath", "//button[@class= 'button-1 register-next-step-button']").click()

    def Logout(self):
        self.driver.find_element("xpath", "//a[@class= 'ico-logout']").click()
