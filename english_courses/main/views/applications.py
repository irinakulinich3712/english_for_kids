from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from ..models import Application


def applications(request):
    applications_list = Application.objects.order_by('created_at')
    return render(request, 'main/applications.html', {'applications': applications_list})


def one_application(request, ap_id):
    try:
        application_obj = Application.objects.get(id=ap_id)
    except ObjectDoesNotExist:
        return HttpResponse("This application could not be found")
    return render(request, 'main/application.html', {'application': application_obj})
