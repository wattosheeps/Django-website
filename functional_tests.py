from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
class firstVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_create_a_new_CV(self):
        #User visits the homepage
        self.browser.get('http://localhost:8000/cv')
        #User can see that CV is a title on the home page and a header
        
        #User clicks on the "Update summary" button to add a summary of the user

        #Types in "Generic summary" into the text box

        #Updates the page by hitting enter, and now the page shows the updated summary

        #User clicks on the "Update summary" button again, and this time sees the current
        #summary already used as a placeholder in the textbox

        #The user makes another update to the summary and hits enter again to see the change
        self.fail('Finish the test!')
if __name__ == '__main__':
    unittest.main(warnings='ignore')