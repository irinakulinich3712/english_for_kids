from django.shortcuts import render
from ..models import Application


def applications(request):
    applications_list = Application.objects.order_by('created_at')
    return render(request, 'main/applications.html', {'applications': applications_list})