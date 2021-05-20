from django.urls import path
from .views import all_students, announcements, applications, groups, home, lessons, student_account, \
    observations, authentication

urlpatterns = [
    path('', home.index, name='home'),
    path('groups/', groups.all_groups, name='groups'),
    path('groups/<int:g_id>/students/', groups.group_students, name='group_students'),
    path('groups/<int:g_id>/delete-group/', groups.delete_group, name='delete_group'),
    path('groups/<int:g_id>/delete-student-from-group/<int:s_id>/', groups.delete_student_from_group,
         name='delete_student_from_group'),

    path('groups/<int:g_id>/lessons/', lessons.lessons, name='lessons'),
    path('groups/<int:g_id>/lessons/delete-lesson/<int:l_id>/', lessons.delete_lesson, name='delete_lesson'),

    path('announcements/', announcements.announcements, name='announcements'),
    path('announcements/delete-announcement/<int:an_id>/', announcements.delete_announcement,
         name='delete_announcement'),

    path('applications/', applications.applications, name='applications'),
    path('applications/<int:ap_id>', applications.one_application, name='application'),
    path('applications/delete-application/<int:ap_id>/', applications.delete_application, name='delete_application'),


    path('students/', all_students.all_students, name='all_students'),
    path('students/<int:s_id>/', student_account.student_account, name='student_account'),
    path('students/<int:s_id>/observations/', observations.observations, name='observations'),
    path('students/<int:s_id>/delete-observation/<int:o_id>/', observations.delete_observation,
         name='delete_observation'),
    path('students/<int:s_id>/delete-student/', student_account.delete_student, name='delete_student'),
]
