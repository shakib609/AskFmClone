from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.CharField(max_length=300, default=None)
    asked_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='asked_to_questions')
    asked_by = models.ForeignKey(User, default=None, null=True,
                                 related_name='asked_by_questions')
    time = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:40]


class Answer(models.Model):
    text = models.TextField(default=None)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:40]
