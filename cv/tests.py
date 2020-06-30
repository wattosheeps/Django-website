from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import resolve
from cv.views import cv_page
from cv.views import edit_summary
from cv.views import new_education
from cv.models import Summary
from cv.models import Qualification
from cv.views import new_experience
from cv.models import Experience
from cv.models import Skill
from django.db import models
from django.utils import timezone
from django.contrib.auth import authenticate
# Create your tests here.
class cvPageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)
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

class educationPageTest(TestCase):
    def test_button_has_correct_url_redirect(self):
        response = self.client.get('/cv/')
        html = response.content.decode('utf8')
        self.assertIn('href="new-education"',html)
        found = resolve('/cv/new-education')
        self.assertEqual(found.func, new_education)

class experiencePageTest(TestCase):
    def test_returns_correct_html(self):
        response = self.client.get('/cv/new-experience')
        html = response.content.decode('utf8')  
        self.assertTemplateUsed(response, 'cv\edit_experience.html')
    def test_button_has_correct_url_redirect(self):
        response = self.client.get('/cv/')
        html = response.content.decode('utf8')
        self.assertIn('href="new-experience"',html)
        found = resolve('/cv/new-experience')
        self.assertEqual(found.func, new_experience)
class SummaryModelTest(TestCase):
    def test_saving_and_retrieving_summary(self):
        summary = Summary()
        summary.text = "Generic Summary"
        summary.save()

        saved_items = Summary.objects.all()
        self.assertEqual(saved_items.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.text, 'Generic Summary')
class QualificationsModelTest(TestCase):
    def test_saving_and_retrieving_qualification(self):
        qualification = Qualification()
        """ 
        qualification.date_start = models.DateField()
        qualification.date_end = models.DateField() """
        qualification.location = "test street"
        qualification.description = "Generic description"
        qualification.save()

        qualification2 = Qualification()
        """ qualification2.date_start = models.DateField()
        qualification2.date_end = models.DateField() """
        qualification2.location = "test road"
        qualification2.description = "more unique description"
        qualification2.save()
        saved_items = Qualification.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        """ self.assertEqual(str(first_saved_item.start_date), str(models.DateField(models.DateField.auto_now_add)))
         """
        self.assertEqual(first_saved_item.location, 'test street')
        self.assertEqual(first_saved_item.description, 'Generic description')

        """ self.assertEqual(str(second_saved_item.start_date), str(models.DateField(models.DateField.auto_now_add)))
        """ 
        self.assertEqual(second_saved_item.location, 'test road')
        self.assertEqual(second_saved_item.description, 'more unique description')

class ExperienceModelTest(TestCase):
    def test_and_retrieve_experience(self):
        experience = Experience()
        """ experience.date_start = models.DateField()
        experience.date_end = models.DateField() """
        experience.location = "test street"
        experience.duties = "making coffee"
        experience.description = "Generic description"
        experience.save()

        experience2 = Experience()
        """ experience2.date_start = models.DateField()
        experience2.date_end = models.DateField() """
        experience2.location = "test road"
        experience2.duties = "doing important things"
        experience2.description = "more unique description"
        experience2.save()
        saved_items = Experience.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        """ self.assertEqual(str(first_saved_item.date_start), str(models.DateField(models.DateField.auto_now_add)))
         """
        self.assertEqual(first_saved_item.location, 'test street')
        self.assertEqual(first_saved_item.duties, 'making coffee')
        self.assertEqual(first_saved_item.description, 'Generic description')

        """ self.assertEqual(str(second_saved_item.date_start), str(models.DateField(models.DateField.auto_now_add)))
         """
        self.assertEqual(second_saved_item.location, 'test road')
        self.assertEqual(second_saved_item.duties, 'doing important things')
        self.assertEqual(second_saved_item.description, 'more unique description')

class SkillsModelTest(TestCase):
    def test_and_retrieve_experience(self):
        skill = Skill()
        skill.heading = "New Heading 1"
        skill.info = "INFO"
        skill.save()

        skill2 = Skill()
        skill2.heading = "New Heading 2"
        skill2.info = "INFO"
        skill2.save()
        saved_items = Skill.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.heading, 'New Heading 1')
        self.assertEqual(first_saved_item.info, 'INFO')

        self.assertEqual(second_saved_item.heading, 'New Heading 2')
        self.assertEqual(second_saved_item.info, 'INFO')