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
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.clear()
        inputbox.send_keys('jimbob')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.clear()
        inputbox.send_keys('yd9VcBZX9yWsjeK')
        self.browser.find_element_by_id('login_button').click()
        self.browser.get('http://127.0.0.1:8000/cv/')
        #User can see that CV is a title on the home page and a header
        self.assertIn('CV',self.browser.title)
        time.sleep(10)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Archie Watson', header_text)
        #User clicks on the "Update summary" button to add a summary of the user
        self.browser.find_element_by_id('summary_button').click()
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
        self.browser.find_element_by_id('summary_button').click()
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
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.clear()
        inputbox.send_keys('jimbob')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.clear()
        inputbox.send_keys('yd9VcBZX9yWsjeK')
        self.browser.find_element_by_id('login_button').click()
        self.browser.get('http://127.0.0.1:8000/cv/')
        #The user can see a section with the heading "Education and Qualifications"
        heading = self.browser.find_element_by_id('id_education_heading')
        self.assertEqual(heading.text,"Education and Qualifications")
        #The user clicks the "Add" button
        self.browser.find_element_by_id('education_button').click()
        #The user types in the date, location, and description
        date_start = self.browser.find_element_by_id('id_date_start')
        date_start.clear()
        date_start.send_keys('2018-02-19')
        date_end = self.browser.find_element_by_id('id_date_end')
        date_end.clear()
        date_end.send_keys('2018-02-19')
        location = self.browser.find_element_by_id('id_location')
        location.clear()
        location.send_keys('test town')
        description = self.browser.find_element_by_id('id_description')
        description.clear()
        description.send_keys('Generic description')
        
        time.sleep(1)
        #The user clicks "submit" and is taken back to the main page
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
        
        #The user can now see the listings
        
        newListing = self.browser.find_element_by_link_text('test town')
        time.sleep(1)
        #The user then clicks on their uploaded qualification
        self.browser.get(newListing.get_attribute("href"))
        time.sleep(1)
        #The user is taken to another page, where they are able to edit the data
        location = self.browser.find_element_by_id('id_description')
        self.assertEqual('Generic description',location.text)
        #The user changes the date
        date_start = self.browser.find_element_by_id('id_date_start')
        date_start.clear()
        date_start.send_keys('2019-05-12')
        date_end = self.browser.find_element_by_id('id_date_end')
        date_end.clear()
        date_end.send_keys('2020-09-20')
        #The user clicks submit
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
        #The user is now returned to the overview page where they can now see their updated listing

        
    def test_input_work_experience(self):
        #User visits the home page
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.clear()
        inputbox.send_keys('jimbob')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.clear()
        inputbox.send_keys('yd9VcBZX9yWsjeK')
        self.browser.find_element_by_id('login_button').click()
        self.browser.get('http://127.0.0.1:8000/cv/')
        #User can see the section labelled 'work experience'
        heading = self.browser.find_element_by_id('id_experience_heading')
        self.assertEqual(heading.text,"Work Experience")
        #User clicks the add new button and is sent to a new page
        self.browser.find_element_by_id('experience_button').click()
        #User then inputs the required details
        date_start = self.browser.find_element_by_id('id_date_start')
        date_start.clear()
        date_start.send_keys('2019-04-09')
        date_end = self.browser.find_element_by_id('id_date_end')
        date_end.clear()
        date_end.send_keys('2020-04-09')
        location = self.browser.find_element_by_id('id_location')
        location.clear()
        location.send_keys('test limited')
        duties = self.browser.find_element_by_id('id_duties')
        duties.clear()
        duties.send_keys('Generic Duties')
        description = self.browser.find_element_by_id('id_description')
        description.clear()
        description.send_keys('Generic description')
        
        time.sleep(1)
        #User presses submit
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
        #User can now see the data listed on the main page
        newListing = self.browser.find_element_by_link_text('test limited')
        #User clicks on the recently uploaded work experience
        self.browser.get(newListing.get_attribute("href"))
        #The user is taken to the same page as before, but now the data is already found in the input boxes
        description = self.browser.find_element_by_id('id_description')
        self.assertEqual('Generic description',description.text)
        #The user changes the date
        date_start = self.browser.find_element_by_id('id_date_start')
        date_start.clear()
        date_start.send_keys('2019-02-09')
        date_end = self.browser.find_element_by_id('id_date_end')
        date_end.clear()
        date_end.send_keys('2020-01-24')
        #The user clicks submit
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()

        #User can see this data has now been edited
    def test_input_skill(self):
        #User visits the home page
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.clear()
        inputbox.send_keys('jimbob')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.clear()
        inputbox.send_keys('yd9VcBZX9yWsjeK')
        self.browser.find_element_by_id('login_button').click()
        self.browser.get('http://127.0.0.1:8000/cv/')
        #User can see the section labelled 'work experience'
        heading = self.browser.find_element_by_id('id_skills_heading')
        self.assertEqual(heading.text,"Additional Skills and Information")
        #User clicks the add new button and is sent to a new page
        self.browser.find_element_by_id('skills_button').click()
        #User then inputs the required details
        
        heading = self.browser.find_element_by_id('id_heading')
        heading.clear()
        heading.send_keys('new heading')
        info = self.browser.find_element_by_id('id_info')
        info.clear()
        info.send_keys('Generic skill')
        
        time.sleep(1)
        #User presses submit
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
        #User can now see the data listed on the main page
        newListing = self.browser.find_element_by_link_text('new heading')
        #User clicks on the recently uploaded work experience
        self.browser.get(newListing.get_attribute("href"))
        #The user is taken to the same page as before, but now the data is already found in the input boxes
        description = self.browser.find_element_by_id('id_info')
        self.assertEqual('Generic skill',description.text)
        #The user changes the description
        description.send_keys('New skill')
        #The user clicks submit
        self.browser.find_element_by_xpath('//button[text()="Save"]').click()
if __name__ == '__main__':
    unittest.main(warnings='ignore')