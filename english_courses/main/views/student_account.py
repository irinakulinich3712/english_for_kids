from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from ..models import Student, StudentGroup, Observation
from django.http import HttpResponse


def student_account(request, s_id):
    try:
        student_object = Student.objects.select_related('user').values('user_id',
                                                                       'user__first_name',
                                                                       'user__last_name',
                                                                       'user__email',
                                                                       'parent_tel_numb',
                                                                       'parent_f_name',
                                                                       'parent_patronimic',
                                                                       'parent_l_name',
                                                                       'student_group_id').get(user_id=s_id)

        student = dict(id=student_object['user_id'], first_name=student_object['user__first_name'],
                       last_name=student_object['user__last_name'],
                       parent_tel_numb=student_object['parent_tel_numb'],
                       parent_f_name=student_object['parent_f_name'],
                       parent_patronimic=student_object['parent_patronimic'],
                       parent_l_name=student_object['parent_l_name'], email=student_object['user__email'],
                       student_group_id=student_object['student_group_id'], student_group="")

        if student['student_group_id'] is None:
            student['student_group'] = "No group"
        else:
            student['student_group'] = '%s%s' % (StudentGroup.objects.get(id=student['student_group_id']).year,
                                                 StudentGroup.objects.get(id=student['student_group_id']).name)

        return render(request, 'main/student_account.html', {'student': student})
    except ObjectDoesNotExist:
        return HttpResponse("The student could not be found")
