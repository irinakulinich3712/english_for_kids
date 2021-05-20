from django.contrib import messages
from django.shortcuts import render, redirect
from ..models import Observation


def observations(request, s_id):
    observations_list = Observation.objects.filter(student=s_id).order_by('created_at')

    return render(request, 'main/observations.html', {'observations': observations_list})


def delete_observation(request, s_id, o_id):
    observation = Observation.objects.get(id=o_id)
    observation.delete()
    messages.success(request, "An observation has been deleted successfully")
    return redirect('observations', s_id=s_id)
