import testData.logInData


class Login:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        self.driver.find_element("xpath", "//a[@class ='ico-login']").click()

    def log_email(self):
        self.driver.find_element("id", "Email").send_keys(testData.logInData.loginEmail)

    def log_password(self):
        self.driver.find_element("id", "Password").send_keys(testData.logInData.loginPassword)

    def confirmLog(self):
        self.driver.find_element("xpath", "//button[@class = 'button-1 login-button']").click()
