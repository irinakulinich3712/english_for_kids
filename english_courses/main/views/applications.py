from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .all_students import group_check
from ..models import Application


@user_passes_test(group_check)
@login_required
def applications(request):
    applications_list = Application.objects.order_by('-created_at')
    return render(request, 'main/applications.html', {'applications': applications_list})


@user_passes_test(group_check)
@login_required
def one_application(request, ap_id):
    try:
        application_obj = Application.objects.get(id=ap_id)
    except ObjectDoesNotExist:
        return HttpResponse("This application could not be found")
    return render(request, 'main/application.html', {'application': application_obj})


@user_passes_test(group_check)
@login_required
def delete_application(request, ap_id):
    application = Application.objects.get(id=ap_id)
    application.delete()
    messages.success(request, "You have deleted an application successfully")
    return redirect('applications')