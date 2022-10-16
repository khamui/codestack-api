"""Adding endpoint urls for user"""
from django.urls import path

from user import views

# used for reverse() function
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]