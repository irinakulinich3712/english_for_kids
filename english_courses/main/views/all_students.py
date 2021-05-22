from smtplib import SMTPException

from django.conf import settings
import random
import string
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from ..forms import CreateStudentForm
from ..models import Student, StudentGroup


def group_check(user):
    return user.is_superuser or user.groups.filter(name='teacher').exists()


def all_students(request):
    students_list = [dict(
        id=s['user_id'], first_name=s['user__first_name'], last_name=s['user__last_name'],
        student_group_id=s['student_group_id'], student_group="")
        for s in Student.objects.all().select_related('user').values('user_id', 'user__last_name',
                                                                     'user__first_name', 'student_group_id').order_by(
            'user__last_name', 'student_group__year')]

    for s in students_list:
        if s['student_group_id'] is None:
            s['student_group'] = "No group"
        else:
            s['student_group'] = '%s%s' % (StudentGroup.objects.get(id=s['student_group_id']).year,
                                           StudentGroup.objects.get(id=s['student_group_id']).name)

    return render(request, 'main/all_students.html', {'students': students_list})


def new_student(request):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    if request.method == 'POST':
        create_form = CreateStudentForm(request.POST)
        if create_form.is_valid():
            password_string = ''.join(random.choice(password_characters) for i in range(10))
            password = make_password(password_string, hasher='default')
            create_form.save(password)
            user = create_form.cleaned_data.get('username')
            user_email = create_form.cleaned_data.get('email')
            try:
                send_mail("English for kids student account credentials",
                          'Username: %s; Password: %s' % (user, password_string),
                          settings.EMAIL_HOST_USER,
                          [user_email], fail_silently=False)
            except SMTPException:
                messages.error(request, 'There was a problem with sending e-mail')

            messages.success(request, 'Account was created for ' + user)
            return redirect('all_students')
        else:
            messages.error(request, 'The form has been filled incorrectly')

    else:
        create_form = CreateStudentForm()
    context = {
        'create_form': create_form
    }

    return render(request, 'main/new_student.html', {'create_form': context['create_form']})
