from django.urls import path
from .views import all_students, announcements, applications, groups, home, lessons, student_account, \
    observations, authentication

urlpatterns = [
    path('', home.index, name='home')
]
