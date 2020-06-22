from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
class firstVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def check_for_row_in_list_table(self, row_text):
        summary = self.browser.find_element_by_id('id_summary')
        self.assertEquals(row_text, summary.text)
    def test_can_create_a_new_CV(self):
        #User visits the homepage
        self.browser.get('http://127.0.0.1:8000/cv')
        #User can see that CV is a title on the home page and a header
        self.assertIn('CV',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CV', header_text)
        #User clicks on the "Update summary" button to add a summary of the user
        self.browser.find_element_by_xpath('//button[text()="Update Summary"]').click()
        time.sleep(1)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Summary', header_text)
        #Types in "Generic summary" into the text box
        inputbox = self.browser.find_element_by_id('id_text')
        inputbox.clear()
        inputbox.send_keys('Generic summary')
        #Updates the page by hitting enter, and now the page shows the updated summary
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
        time.sleep(1)
        self.check_for_row_in_list_table('Generic summary')
        #User clicks on the "Update summary" button again, and this time sees the current
        #summary already used as a placeholder in the textbox

        #The user makes another update to the summary and hits enter again to see the change
        self.fail('Finish the test!')
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')