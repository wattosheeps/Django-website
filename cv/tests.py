from django.test import TestCase
from django.urls import resolve
from cv.views import cv_page
from django.http import HttpRequest
# Create your tests here.
class cvPageTest(TestCase):
    def test_url_resolves_to_cv_page_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_page)
    def test_returns_correct_html(self):
        request = HttpRequest()  
        response = cv_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>CV</title>', html)  
        self.assertTrue(html.endswith('</html>'))