from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Question


@login_required
def my_profile_view(request):
    unanswered_questions = Question.objects.filter(
                                asked_to=request.user,
                                answer=None).select_related(
                                                'asked_by').order_by('-time')
    asked_questions = Question.objects.filter(
                            asked_by=request.user).order_by('-time')
    context = {
        'unanswered_questions': unanswered_questions,
        'asked_questions': asked_questions
    }
    return render(request, 'askfm/my_profile_view.html', context)


def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        return redirect('askfm:my_profile_view')

    answered_questions = Question.objects.exclude(answer=None).filter(
                              asked_to=user).select_related(
                                  'answer').order_by('-time')

    asked_questions = Question.objects.filter(asked_by=user).select_related(
                              'answer').order_by('-time')

    context = {
        'username': username,
        'answered_questions': answered_questions,
        'asked_questions': asked_questions
    }
    return render(request, 'askfm/user_profile_view.html', context)


@login_required
def answer_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return
