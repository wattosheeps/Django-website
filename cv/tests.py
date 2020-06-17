from django.test import TestCase
from django.urls import resolve
from cv.views import cv_page
# Create your tests here.
class cvPageTest(TestCase):
    def test_url_resolves_to_cv_page_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_page)