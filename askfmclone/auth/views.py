from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,\
                                login as djlogin, logout as djlogout
from django.contrib.auth.models import User
from django.contrib import messages

import re

from .forms import LoginForm, RegistrationForm


def login(request):
    if request.user.is_authenticated():
        return redirect(reverse('askfm:my_profile_view'))
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
                djlogin(request, user)
                next_page = request.GET.get(
                                'next') or reverse('askfm:my_profile_view')
                messages.success(request, 'Logged in Successfully!')
                return redirect(next_page)
            messages.error(request, 'Wrong username or password',
                           extra_tags='danger')
    form = LoginForm()
    return render(request, 'auth/login_view.html', {'form': form})


def logout(request):
    if request.user.is_authenticated():
        djlogout(request)
        messages.success(request, 'Logged out successfully!')
    return redirect(reverse('askfm:homepage'))


def registration(request):
    next_page = request.GET.get('next') or reverse('askfm:my_profile_view')
    if request.user.is_authenticated():
        return redirect(next_page)

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
            djlogin(request, user)
            messages.success(
                request, 'Your Account has been created successfully.')
            return redirect(next_page)
    else:
        form = RegistrationForm()
    return render(request, 'auth/registration_view.html', {'form': form})
