from django.shortcuts import render
from ..models import Student, StudentGroup


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