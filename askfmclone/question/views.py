from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Question


def details(request, question_id):
    if request.user.is_authenticated():
        question = get_object_or_404(
            Question,
            id=question_id,
            asked_by=request.user
        )
        context = {
            'question': question
        }
        return render(request, 'question/details.html', context)
    else:
        messages.error(request, 'Something went wrong!', extra_tags='danger')
        return redirect(reverse('askfm:my_profile_view'))
