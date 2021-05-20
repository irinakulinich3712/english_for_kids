from datetime import datetime, timedelta

from django.contrib import messages
from django.shortcuts import render, redirect
from ..models import Announcement


def announcements(request):
    announcements_list = Announcement.objects.filter(
        created_at__gte=datetime.now() - timedelta(days=60)).order_by(
        'created_at')

    return render(request, 'main/announcements.html', {'announcements': announcements_list})


def delete_announcement(request, an_id):
    announcement = Announcement.objects.get(id=an_id)
    announcement.delete()
    messages.success(request, 'You have deleted the announcement successfully')
    return redirect('announcements')
