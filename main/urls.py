from django.urls import path
from .views import all_students, announcements, applications, groups, home, lessons, student_account, \
    observations, authentication

urlpatterns = [
    path('', home.index, name='home'),
    path('choose-student/', groups.choose_student, name='choose_student'),

    path('groups/', groups.all_groups, name='groups'),
    path('groups/<int:g_id>/', groups.group, name='group'),
    path('groups/<int:g_id>/students/', groups.group_students, name='group_students'),
    path('groups/<int:g_id>/students/add-student/<int:s_id>/', groups.add_student_to_group, name='add_student_to_group'),
    path('groups/<int:g_id>/delete-group/', groups.delete_group, name='delete_group'),
    path('groups/<int:g_id>/delete-student-from-group/<int:s_id>/', groups.delete_student_from_group,
         name='delete_student_from_group'),

    path('groups/<int:g_id>/lessons/', lessons.lessons, name='lessons'),
    path('groups/<int:g_id>/lessons/delete-lesson/<int:l_id>/', lessons.delete_lesson, name='delete_lesson'),
    path('groups/<int:g_id>/lessons/edit-lesson/<int:l_id>/', lessons.edit_lesson, name='edit_lesson'),

    path('students/', all_students.all_students, name='all_students'),
    path('students/new-student/', all_students.new_student, name='new_student'),

    path('announcements/', announcements.announcements, name='announcements'),
    path('announcements/edit-announcement/<int:an_id>/', announcements.edit_announcement, name='edit_announcement'),
    path('announcements/delete-announcement/<int:an_id>/', announcements.delete_announcement, name='delete_announcement'),

    path('applications/', applications.applications, name='applications'),
    path('applications/<int:ap_id>', applications.one_application, name='application'),
    path('applications/delete-application/<int:ap_id>/', applications.delete_application, name='delete_application'),

    path('students/<int:s_id>/', student_account.student_account, name='student_account'),
    path('students/<int:s_id>/delete-student/', student_account.delete_student, name='delete_student'),
    path('students/<int:s_id>/edit-student/', student_account.edit_student, name='edit_student'),

    path('students/<int:s_id>/edit-observation/<int:o_id>/', observations.edit_observation, name='edit_observation'),
    path('students/<int:s_id>/observations/', observations.observations, name='observations'),
    path('students/<int:s_id>/delete-observation/<int:o_id>/', observations.delete_observation,
         name='delete_observation'),


    path('login/', authentication.login_user, name='login'),
    path('logout/', authentication.logout_user, name='logout')
]