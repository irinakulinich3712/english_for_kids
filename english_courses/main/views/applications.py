from django.shortcuts import render
from ..models import Application


def applications(request):
    applications_list = Application.objects.order_by('created_at')
    return render(request, 'main/applications.html', {'applications': applications_list})


def one_application(request, ap_id):
    application_obj = Application.objects.get(id=ap_id)
    return render(request, 'main/application.html', {'applications_list': application_obj})
