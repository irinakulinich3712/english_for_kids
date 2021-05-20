from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import StudentGroup, Student


def all_groups(request):
    groups_list = [dict(id=s_group.id, year=s_group.year, name=s_group.name,
                        student_count=len(Student.objects.filter(student_group_id=s_group.id))) for s_group in
                   StudentGroup.objects.all()]

    return render(request, 'main/all_groups.html', {'groups': groups_list})


def group(request, g_id):
    try:
        group_obj = StudentGroup.objects.get(id=g_id)

        students_list = Student.objects.filter(student_group_id=g_id). \
            select_related('user').values('user_id',
                                          'user__last_name',
                                          'user__first_name').order_by('user__last_name')

        return render(request, 'main/group.html', {'group': group_obj, 'students': students_list})
    except ObjectDoesNotExist:
        return HttpResponse("This group could not be found")
