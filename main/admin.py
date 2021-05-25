from django.contrib import admin
from .models import Application, CustomUser, StudentGroup, Lesson, Announcement, Observation,\
    Student
from django.contrib.auth.admin import UserAdmin

admin.site.register(Application)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Announcement)
admin.site.register(StudentGroup)
admin.site.register(Lesson)
admin.site.register(Observation)
admin.site.register(Student)