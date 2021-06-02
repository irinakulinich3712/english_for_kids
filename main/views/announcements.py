from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect

from .all_students import group_check
from ..forms import CreateAnnouncementForm, EditAnnouncementForm
from ..models import Announcement


@user_passes_test(group_check)
@login_required
def announcements(request):
    """
    Renders the announcements page, with a list of all announcements created within the last 60 days
    and forms for creating and editing an announcement.
    """
    announcements_list = Announcement.objects.filter(created_at__gte=datetime.now() - timedelta(days=60))
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


@user_passes_test(group_check)
@login_required
def edit_announcement(request, an_id):
    """
    Processes the form for editing an announcement.
    Redirects to the announcements page, with list of the latest announcements.
    Args: an_id: the id of the announcement being edited.
    """
    obj = Announcement.objects.get(id=an_id)

    if request.method == 'POST':
        edit_form = EditAnnouncementForm(request.POST, instance=obj)

        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'You have edited the announcement successfully')
        else:
            messages.error(request, 'You have not filled the form correctly')

    return redirect('announcements')


@user_passes_test(group_check)
@login_required
def delete_announcement(request, an_id):
    """
    Deletes the chosen announcement.
    Args: an_id: the id of the chosen announcement.
    """
    announcement = Announcement.objects.get(id=an_id)
    announcement.delete()
    messages.success(request, 'You have deleted the announcement successfully')
    return redirect('announcements')
