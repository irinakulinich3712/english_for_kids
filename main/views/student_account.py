from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from .all_students import group_check
from ..forms import EditUserForm, EditStudentForm
from ..models import Student, StudentGroup, CustomUser
from django.http import HttpResponse


@user_passes_test(group_check)
@login_required
def student_account(request, s_id):
    try:
        student_object = Student.objects.select_related('user').values('user_id',
                                                                       'user__username',
                                                                       'user__first_name',
                                                                       'user__last_name',
                                                                       'user__email',
                                                                       'parent_tel_numb',
                                                                       'parent_f_name',
                                                                       'parent_patronimic',
                                                                       'parent_l_name',
                                                                       'student_group_id').get(user_id=s_id)

        student = dict(id=student_object['user_id'], username=student_object['user__username'],
                       first_name=student_object['user__first_name'],
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


@user_passes_test(group_check)
@login_required
def edit_student(request, s_id):
    user = CustomUser.objects.get(id=s_id)
    student = Student.objects.get(user_id=s_id)

    if request.method == 'POST':
        user_edit_form = EditUserForm(request.POST, instance=user)
        student_edit_form = EditStudentForm(request.POST, instance=student)

        if user_edit_form.is_valid() and student_edit_form.is_valid():
            user_edit_form.save()
            student_edit_form.save()
            messages.success(request, "The student's account has been edited successfully")
            return redirect('student_account', s_id=s_id)
        else:
            messages.error(request, "The form has not been filled correctly")

    else:
        user_edit_form = EditUserForm(instance=user)
        student_edit_form = EditStudentForm(instance=student)

    context = {
        'user_edit_form': user_edit_form,
        'student_edit_form': student_edit_form
    }
    return render(request, 'main/edit_student.html', {'user_edit_form': context['user_edit_form'],
                                                      'student_edit_form': context['student_edit_form']})


@user_passes_test(group_check)
@login_required
def delete_student(request, s_id):
    user = CustomUser.objects.get(id=s_id)
    user.delete()
    messages.success(request, "The student has been deleted successfully")
    return redirect('all_students')

