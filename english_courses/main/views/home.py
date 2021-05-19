from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from ..models import Announcement


def index(request):
    announcements_list = Announcement.objects.filter(created_at__gte=datetime.now() - timedelta(days=60)).order_by(
        'created_at')

    return render(request, 'main/index.html', {'announcements': announcements_list})
