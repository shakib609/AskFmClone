from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

import re

from .forms import LoginForm, RegistrationForm


def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            if re.compile(r'@').search(username_or_email):
                email = username_or_email
                username = User.objects.filter(email=email).first().username
            else:
                username = username_or_email
            user = authenticate(
                       username=username,
                       password=form.cleaned_data['password']
                   )
            if user is not None and user.is_active:
                # TODO: Improve here
                login(request, user)
                next_page = request.POST['next'] or '/'
                messages.success(request, 'Logged in Successfully!')
                return redirect(next_page)
            messages.error(request, 'Wrong username or password',
                           extra_tags='danger')
    form = LoginForm()
    return render(request, 'user/login_view.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('/')


def registration_view(request):
    if request.user.is_authenticated():
        return redirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                   )
            user = authenticate(
                        username=username, password=password
                   )
            login(request, user)
            messages.success(
                request, 'Your Account has been created successfully.')
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'user/registration_view.html', {'form': form})
