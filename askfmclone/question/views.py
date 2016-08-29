from django.shortcuts import render, get_object_or_404

from .models import Question


def details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, 'question/details.html', context)
