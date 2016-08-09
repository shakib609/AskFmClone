from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.CharField(max_length=300, default=None)
    asked_to = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='asked_user')
    asked_by = models.OneToOneField(User,
                                    default=None,
                                    related_name='asking_user')

    def __str__(self):
        return self.text[:40]


class Answer(models.Model):
    text = models.TextField(default=None)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:40]
