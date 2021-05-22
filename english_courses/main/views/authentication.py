from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from ..forms import LoginForm
from ..models import Student


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'You have been logged in successfully')
                    if user.groups.filter(name='teacher').exists():
                        return redirect('groups')
                    if user.groups.filter(name='student').exists():
                        return redirect('observations', s_id=user.id)
                else:
                    messages.error(request, 'Disabled account')
        else:
            messages.error(request, 'You have not filled the form correctly')
    else:
        form = LoginForm()
    context = {
        'form': form
    }

    return render(request, 'main/login.html', {'form': context['form']})


def logout_user(request):
    logout(request)
    return redirect('login')
