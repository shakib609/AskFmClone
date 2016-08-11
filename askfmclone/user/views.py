from django.shortcuts import redirect
# from django.core.urlresolvers import reverse
from django.contrib.auth.views import logout as django_logout,\
                                      login as django_login,\
                                      login_required


def login(request, *args, **kwargs):
    if request.user.is_authenticated():
        # TODO: write static views
        return redirect('/')
    else:
        return django_login(request, *args, **kwargs)


@login_required
def logout(request):
    django_logout(request)
    # TODO: write static views
    return redirect('/')
