from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_page, name='cv_page'),
    path('edit-summary',views.edit_summary, name="edit_summary"),
    ##path('education-overview',views.education_overview, name="education_overview"),
    path('new-education',views.new_education, name="new_education"),
    path('education-edit/<int:pk>/', views.edit_education, name='edit_education'),
    path('new-experience',views.new_experience, name='new_expereince'),
    path('edit-experience/<int:pk>/',views.edit_experience,name='edit_experience')
]