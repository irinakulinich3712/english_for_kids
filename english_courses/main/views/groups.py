from django.contrib import messages
from django.shortcuts import render, redirect
from ..models import StudentGroup


def all_groups(request):
    group_names = StudentGroup.objects.order_by('year')

    return render(request, 'main/all_groups.html', {'group_names': group_names})
