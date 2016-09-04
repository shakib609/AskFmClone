from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Question(models.Model):
    """Question Model
    - Every question has a CharField(text)
    - Every question has two ForeignKeys(asked_by, asked_to)
    - Every question has a DateTimeField(time)
    - Every question has a BooleanField(anonymous)
    """
    text = models.CharField(max_length=300, default=None)
    asked_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='asked_to_questions')
    asked_by = models.ForeignKey(User, default=None, null=True,
                                 related_name='asked_by_questions')
    time = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:40]

    def clean(self):
        if self.asked_by == self.asked_to:
            raise ValidationError(
                '%s cannot ask a question to himself' % self.asked_by.username
            )

    def save(self, *args, **kwargs):
        self.clean()
        return super(Question, self).save(*args, **kwargs)

    def total_likes(self):
        """Returns the total likes count"""
        return self.likes.count()


class Answer(models.Model):
    """Answer Model
    - Every answer has a TextField(text)
    - Every answer has a DateTimeField(asked_at)
    - Every question has only one Answer"""
    text = models.TextField(default=None)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:40]


class Like(models.Model):
    """Like Model
    - Every Question has many likes
    - A Question cannot be liked by the same user twice"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Q# %d liked_by %s' % (
            self.question.id,
            self.liked_by.username
        )

    class Meta:
        unique_together = (('question', 'liked_by'),)
        default_related_name = 'likes'
