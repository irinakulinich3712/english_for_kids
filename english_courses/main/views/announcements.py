from datetime import datetime, timedelta

from django.contrib import messages
from django.shortcuts import render, redirect

from ..forms import CreateAnnouncementForm, EditAnnouncementForm
from ..models import Announcement


def announcements(request):
    announcements_list = Announcement.objects.filter(created_at__gte=datetime.now() - timedelta(days=60)).order_by(
        'created_at')
    edit_form = EditAnnouncementForm()

    if request.method == 'POST':
        create_form = CreateAnnouncementForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, 'You have added an announcement successfully')
            return redirect('announcements')
        else:
            messages.error(request, 'You have not filled the form correctly')

    else:
        create_form = CreateAnnouncementForm()

    context = {
        'create_form': create_form,
        'edit_form': edit_form
    }

    return render(request, 'main/announcements.html', {'announcements': announcements_list,
                                                       'create_form': context['create_form'],
                                                       'edit_form': context['edit_form']})


def delete_announcement(request, an_id):
    announcement = Announcement.objects.get(id=an_id)
    announcement.delete()
    messages.success(request, 'You have deleted the announcement successfully')
    return redirect('announcements')
