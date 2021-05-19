from django.shortcuts import render
from ..models import Observation


def observations(request, s_id):
    observations_list = Observation.objects.filter(student=s_id).order_by('created_at')

    return render(request, 'main/observations.html', {'observations': observations_list})