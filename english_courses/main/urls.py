from django.urls import path
from .views import all_students, announcements, applications, groups, home, lessons, student_account, \
    observations, authentication

urlpatterns = [
    path('', home.index, name='home'),
    path('groups/', groups.all_groups, name='groups'),
    path('groups/<int:g_id>/students/', groups.group_students, name='group_students'),

    path('groups/<int:g_id>/lessons/', lessons.lessons, name='lessons'),

    path('announcements/', announcements.announcements, name='announcements'),

    path('applications/', applications.applications, name='applications'),
    path('applications/<int:ap_id>', applications.one_application, name='application'),

    path('students/', all_students.all_students, name='all_students'),
    path('students/<int:s_id>/', student_account.student_account, name='student_account'),
    path('students/<int:s_id>/observations/', observations.observations, name='observations')
]
