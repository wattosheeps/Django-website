from django.test import TestCase
from django.urls import resolve
from cv.views import cv_page
from cv.views import edit_summary
from cv.models import Summary
# Create your tests here.
class cvPageTest(TestCase):
    def test_url_resolves_to_cv_page_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_page)
    def test_returns_correct_html(self):
        response = self.client.get('/cv/')
        html = response.content.decode('utf8')  
        self.assertTemplateUsed(response, 'cv\cv_page.html')
    def test_button_has_correct_url_redirect(self):
        response = self.client.get('/cv/')
        html = response.content.decode('utf8')
        self.assertIn('href="edit-summary"',html)
        found = resolve('/cv/edit-summary')
        self.assertEqual(found.func, edit_summary)
    def test_shows_correct_summary(self):
        Summary.objects.create(text='Generic Summary')
        saved_items = Summary.objects.all()
        self.assertEqual(saved_items.count(), 1)
        response = self.client.get('/cv/')
        
        self.assertIn('Generic Summary', response.content.decode())
class SummaryModelTest(TestCase):
    def test_saving_and_retrieving_summary(self):
        summary = Summary()
        summary.text = "Generic Summary"
        summary.save()

        saved_items = Summary.objects.all()
        self.assertEqual(saved_items.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.text, 'Generic Summary')