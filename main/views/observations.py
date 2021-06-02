from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect

from .all_students import group_check
from ..forms import EditObservationForm, CreateObservationForm
from ..models import Observation, CustomUser, Student


@login_required
def observations(request, s_id):
    """
    Renders the observations page, with a list of all observations for the currently viewed student,
    and forms for creating and editing an observation.
    Args: s_id: the id of the student whose account is being viewed.
    """
    if (request.user.id == s_id) or request.user.is_staff:
        observations_list = Observation.objects.filter(student=s_id)
        edit_form = EditObservationForm()

        if request.method == 'POST':
            create_form = CreateObservationForm(request.POST)
            if create_form.is_valid():
                create_form.instance.student = Student.objects.get(user_id=s_id)
                create_form.save()
                messages.success(request, "An observation has been created successfully")
                return redirect('observations', s_id=s_id)
            else:
                messages.error(request, "The form has not been filled correctly")

        else:
            create_form = CreateObservationForm()
        context = {
            'create_form': create_form,
            'edit_form': edit_form,
            'f_name': CustomUser.objects.get(id=s_id).first_name,
            'l_name': CustomUser.objects.get(id=s_id).last_name
        }

        return render(request, 'main/observations.html', {'observations': observations_list,
                                                          'create_form': context['create_form'],
                                                          'edit_form': context['edit_form'],
                                                          'student_id': s_id, 'f_name':context['f_name'],
                                                          'l_name':context['l_name']})
    else:
        return redirect('login')


@user_passes_test(group_check)
@login_required
def edit_observation(request, s_id, o_id):
    """
    Processes the form for editing an observation.
    Redirects to the observations page, with list of observations.
    Args: s_id: the id of the student whose account is being viewed.
          o_id: the id of the chosen observation.
    """
    obj = Observation.objects.get(id=o_id)
    if request.method == 'POST':
        edit_form = EditObservationForm(request.POST, instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, "An observation has been edited successfully")
        else:
            messages.error(request, "The form has been filled in incorrectly")
    return redirect('observations', s_id=s_id)


@user_passes_test(group_check)
@login_required
def delete_observation(request, s_id, o_id):
    """
    Deletes the chosen observation.
    Args: s_id: the id of the student whose account is being edited.
          o_id: the id of the chosen observation.
    """
    observation = Observation.objects.get(id=o_id)
    observation.delete()
    messages.success(request, "An observation has been deleted successfully")
    return redirect('observations', s_id=s_id)
