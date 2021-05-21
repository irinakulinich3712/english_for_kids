from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ..forms import EditGroupForm, CreateGroupForm
from ..models import StudentGroup, Student


def all_groups(request):
    groups_list = [dict(id=s_group.id, year=s_group.year, name=s_group.name,
                        student_count=len(Student.objects.filter(student_group_id=s_group.id))) for s_group in
                   StudentGroup.objects.all()]

    if request.method == 'POST':
        create_form = CreateGroupForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, 'The group has been created successfully')
            return redirect('groups')
        else:
            messages.error(request, 'Please, fill the form correctly')
    else:
        create_form = CreateGroupForm()

    context = {
        'create_form': create_form
    }

    return render(request, 'main/all_groups.html', {'groups': groups_list, 'create_form': context['create_form']})


def group_students(request, g_id):
    try:
        group_obj = StudentGroup.objects.get(id=g_id)
        num = 0
        students_list = []
        for s in Student.objects.filter(student_group_id=g_id).select_related('user').values('user_id',
                                                                                             'user__last_name',
                                                                                             'user__first_name'). \
                order_by('user__last_name'):
            num += 1
            students_list.append(dict(num=num,
                                      id=s['user_id'], first_name=s['user__first_name'],
                                      last_name=s['user__last_name']))

        return render(request, 'main/group_students.html', {'group': group_obj, 'students': students_list})
    except ObjectDoesNotExist:
        return HttpResponse("This group could not be found")


def group(request, g_id):
    try:
        group_obj = StudentGroup.objects.get(id=g_id)
        student_count = len(Student.objects.filter(student_group_id=g_id))

        return render(request, 'main/group.html', {'group': group_obj, 'student_count': student_count})
    except ObjectDoesNotExist:
        return HttpResponse("This group could not be found")


def delete_group(request, g_id):
    group_object = StudentGroup.objects.get(id=g_id)
    group_object.delete()
    messages.success(request, "You have deleted a group successfully")
    return redirect('groups')


def delete_student_from_group(request, g_id, s_id):
    student = Student.objects.get(user_id=s_id)
    student.student_group_id = None
    messages.success(request, "The student has been removed from group")
    student.save()
    return redirect('group_students', g_id=g_id)
