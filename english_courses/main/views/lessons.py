from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from datetime import datetime, timedelta

from ..forms import CreateLessonForm
from ..models import StudentGroup, Lesson
from django.http import HttpResponse


def lessons(request, g_id):
    try:
        group_obj = StudentGroup.objects.get(id=g_id)

        group_lessons_list = Lesson.objects.filter(student_group=g_id,
                                                   created_at__gte=datetime.now() - timedelta(days=60)) \
            .order_by('created_at')

        edit_form = EditLessonForm()

        if request.method == 'POST':
            create_form = CreateLessonForm(request.POST)
            if create_form.is_valid():
                create_form.instance.student_group = StudentGroup.objects.get(id=g_id)
                create_form.save()
                messages.success(request, "The lesson has been created successfully")
            else:
                messages.error(request, "The form has been filled incorrectly")
        else:

            create_form = CreateLessonForm()

        context = {
            'create_form': create_form,
            'edit_form': edit_form
        }

        return render(request, 'main/lessons.html', {'group_lessons': group_lessons_list, 'group': group_obj,
                                                     'create_form': context['create_form'],
                                                     'edit_form': context['edit_form']})
    except ObjectDoesNotExist:
        return HttpResponse("This groups does not exist")


def delete_lesson(request, g_id, l_id):
    try:
        lesson = Lesson.objects.get(id=l_id)
        lesson.delete()
        messages.success(request, "The lesson has been deleted successfully")
    except ObjectDoesNotExist:
        return HttpResponse("The lesson could not be found")
    return redirect('lessons', g_id=g_id)
