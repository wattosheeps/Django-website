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
    def check_for_qualification(self,location,date,id):
        qualification = self.browser.find_element_by_id(id)
        self.assertEquals(location,qualification.location)
        self.assertEquals(date,qualification.date)
    def test_can_update_summary(self):
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
        #Updates the page by clicking save, and now the page shows the updated summary
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
        time.sleep(1)
        self.check_for_row_in_list_table('Generic summary')
        #User clicks on the "Update summary" button again, and this time sees the current
        #summary already used as a placeholder in the textbox
        self.browser.find_element_by_xpath('//button[text()="Update Summary"]').click()
        inputbox = self.browser.find_element_by_id('id_text')
        self.assertEquals("Generic summary", inputbox.text)
        #The user makes another update to the summary and hits enter again to see the change
        inputbox.clear()
        inputbox.send_keys('New summary')
        #Updates the page by clicking save, and now the page shows the updated summary
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
        time.sleep(1)
        self.check_for_row_in_list_table('New summary')
    def test_can_add_new_education_listing(self):
        #User visits the homepage
        self.browser.get('http://127.0.0.1:8000/cv')
        #The user can see a section with the heading "Education and Qualifications"
        heading = self.browser.find_element_by_id('id_education_heading')
        self.assertEqual(heading.text,"Education and Qualifications")
        #The user clicks the heading and is taken to a sepearte page with all the listings
        heading.click()
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Education and Qualifications', header_text)
        time.sleep(2)
        ##self.assertIn('Education and Qualifications',self.browser.title)
        #The user clicks the "Add" button
        self.browser.find_element_by_xpath('//button[text()="Add"]').click()
        #The user types in the date, location, and description
        date = self.browser.find_element_by_id('id_date')
        date.clear()
        date.send_keys('2017 (Jan - Apr)')
        location = self.browser.find_element_by_id('id_location')
        location.clear()
        location.send_keys('test town')
        description = self.browser.find_element_by_id('id_description')
        description.clear()
        description.send_keys('Generic description')
        
        time.sleep(1)
        #The user clicks "submit" and is taken back to the Education and Qualifications page
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
        
        #The user can now see the listings
        newListing = self.browser.find_element_by_link_text('test town')
        #The user then clicks on their uploaded qualification
        newListing.click()
        #The user is taken to another page, where they are able to edit the data
        location = self.browser.find_element_by_id('id_location')
        self.assertEqual('test town',location)
        #The user changes the date
        date = self.browser.find_element_by_id('id_date')
        date.clear()
        date.send_keys(2017 - 2020)
        #The user clicks submit
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
        #The user is now returned to the overview page where they can now see their updated listing

        self.fail('Implement dates properly')
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')