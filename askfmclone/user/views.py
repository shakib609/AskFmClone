from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm


def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                       username=form.cleaned_data['username'],
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
