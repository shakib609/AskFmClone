from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from ..question.models import Question, Answer
from .forms import QuestionForm
from .helpers import get_total_likes


@login_required
def my_profile(request):
    unanswered_questions = Question.objects.filter(
                                asked_to=request.user,
                                answer=None
                            ).select_related('asked_by').order_by('-created')
    asked_questions = Question.objects.filter(
                            asked_by=request.user
                        ).select_related('asked_to').order_by('-created')

    context = {
        'unanswered_questions': unanswered_questions,
        'asked_questions': asked_questions,
        'total_likes': get_total_likes(request.user)
    }
    return render(request, 'askfm/my_profile.html', context)


def homepage(request):
    if not request.user.is_authenticated:
        random_users = User.objects.order_by('?')[:10]
    else:
        random_users = User.objects.order_by('?').exclude(
                username=request.user.username)[:10]
    context = {
        'random_users': random_users
    }
    return render(request, 'askfm/homepage.html', context)


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        return redirect('askfm:my_profile')

    answered_questions = Question.objects.exclude(answer=None).filter(
        asked_to=user).select_related('answer').order_by('-created')

    asked_questions = Question.objects.filter(
        asked_by=user).select_related('answer').order_by('-created')

    if request.method == 'POST':
        if not request.user.is_authenticated():
            messages.error('You must login first!')
            return redirect(
                reverse('auth:login') + '?next=/{}/'.format(username))

        form = QuestionForm(request.POST)
        if form.is_valid():
            q = Question(
                asked_by=request.user,
                asked_to=get_object_or_404(User, username=username),
                text=form.cleaned_data['question_text'],
                anonymous=form.cleaned_data.get('anonymous', False)
            )
            q.save()
            messages.success(request, 'Your question has been submitted!')
            return redirect(reverse('askfm:user_profile', args=(username,)))
    else:
        form = QuestionForm()
    context = {
        'username': username,
        'answered_questions': answered_questions,
        'asked_questions': asked_questions,
        'form': form,
        'total_likes': get_total_likes(user)
    }
    return render(request, 'askfm/user_profile.html', context)


@login_required
@require_POST
def answer(request):
    question_id = request.POST.get('question-id')
    answer_text = request.POST.get('answer-text')

    if question_id and answer_text:
        question = get_object_or_404(
            Question, id=question_id, asked_to=request.user
        )
        answer = Answer.objects.create(text=answer_text, question=question)
        messages.success(request, 'Answer submitted successfully!')
    else:
        messages.error(request, 'Something went wrong.', extra_tags='danger')
    return redirect(reverse('askfm:my_profile'))
