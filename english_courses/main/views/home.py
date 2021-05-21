from datetime import datetime, timedelta

from django.contrib import messages
from django.shortcuts import render, redirect

from ..forms import CreateApplicationForm
from ..models import Announcement


def index(request):
    announcements_list = Announcement.objects.filter(created_at__gte=datetime.now() - timedelta(days=60)).order_by(
        'created_at')

    if request.method == 'POST':
        create_form = CreateApplicationForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, "Your application has been send successfully")
        else:
            messages.error(request, "The form has been filled incorrectly")
    else:
        create_form = CreateApplicationForm()
    context = {
        'create_form': create_form
    }

    return render(request, 'main/index.html', {'announcements': announcements_list,
                                               'create_form': context['create_form']})
