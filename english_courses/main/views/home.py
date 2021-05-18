import datetime

from django.shortcuts import render, redirect
from ..models import Announcement


def index(request):
    announcements = Announcement.objects.filter(created_at__gte=datetime.now() - datetime.timedelta(days=60)).order_by(
        'created_at')

    return render(request, 'main/index.html', {'announcements': announcements})
