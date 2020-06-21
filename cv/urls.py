from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_page, name='cv_page'),
    path('edit-summary',views.edit_summary, name="edit_summary")
]