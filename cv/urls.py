from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_page, name='cv_page'),
    path('edit-summary',views.edit_summary, name="edit_summary"),
    path('education-overview',views.education_overview, name="education_overview"),
    path('new-education',views.new_education, name="new_education")
]