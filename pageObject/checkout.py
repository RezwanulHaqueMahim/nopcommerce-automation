import time

import testData.checkoutData


class CheckOut:
    def __init__(self, driver):
        self.driver = driver

    def checkout_button(self):
        self.driver.find_element("xpath", "//input[@id='termsofservice']").click()
        self.driver.find_element("xpath", "//button[@id='checkout']").click()

    def billing_page(self):
        country = self.driver.find_element("xpath", "//select[@id='BillingNewAddress_CountryId']")
        country.click()
        country.send_keys(testData.checkoutData.country)

        city = self.driver.find_element("xpath", "//input[@id='BillingNewAddress_City']")
        city.click()
        city.send_keys(testData.checkoutData.city)

        address_1 = self.driver.find_element("xpath", "//input[@id='BillingNewAddress_Address1']")
        address_1.click()
        address_1.send_keys(testData.checkoutData.Address1)

        pos_code = self.driver.find_element("xpath", "//input[@id='BillingNewAddress_ZipPostalCode']")
        pos_code.click()
        pos_code.send_keys(testData.checkoutData.pos_code)

        phn = self.driver.find_element("xpath", "//input[@id='BillingNewAddress_PhoneNumber']")
        phn.click()
        phn.send_keys(testData.checkoutData.phn_num)

        cntnue = self.driver.find_element("xpath", "//*[@id='billing-buttons-container']/button[4]")
        cntnue.click()

    def checkout_page(self):
        self.driver.find_element("xpath", "//button[@class='button-1 shipping-method-next-step-button']").click()
        self.driver.find_element("xpath", "//button[@class='button-1 payment-method-next-step-button']").click()
        self.driver.find_element("xpath", "//button[@class='button-1 payment-info-next-step-button']").click()
        self.driver.find_element("xpath", "//button[@class='button-1 confirm-order-next-step-button']").click()
        time.sleep(2)
        self.driver.find_element("xpath", "//button[@class='button-1 order-completed-continue-button']").click()
        time.sleep(2)
        self.driver.close()
