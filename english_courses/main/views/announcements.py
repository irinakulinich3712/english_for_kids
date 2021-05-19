from datetime import datetime, timedelta

from django.shortcuts import render
from ..models import Announcement


def announcements(request):
    announcements_list = Announcement.objects.filter(
        created_at__gte=datetime.now() - timedelta(days=60)).order_by(
        'created_at')

    return render(request, 'main/announcements.html', {'announcements': announcements_list})
