from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_page, name='cv_page'),
    path('edit-summary',views.edit_summary, name="edit_summary"),
    path('new-education',views.new_education, name="new_education"),
    path('education-edit/<int:pk>/', views.edit_education, name='edit_education'),
    path('new-experience',views.new_experience, name='new_expereince'),
    path('edit-experience/<int:pk>/',views.edit_experience,name='edit_experience'),
    path('new-skill',views.new_skill,name='new_skill'),
    path('edit-skill/<int:pk>/',views.edit_skill,name='edit_skill'),
    path('education/<pk>/remove/', views.qualification_remove,name='qualification_remove'),
    path('experience/<pk>/remove/', views.experience_remove,name='experience_remove'),
    path('skill/<pk>/remove/', views.skill_remove,name='skill_remove'),
]