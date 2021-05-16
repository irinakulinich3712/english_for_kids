from django.shortcuts import render, redirect
from ..models import Announcement


def index(request):
    announcements = Announcement.objects.order_by('created_at')

    return render(request, 'main/index.html', {'announcements': announcements})
