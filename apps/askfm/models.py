from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Follow(models.Model):
    following = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed_by = models.ForeignKey(
        User, related_name='followed_by', on_delete=models.CASCADE
    )

    class Meta:
        unique_together = 'following', 'followed_by'

    def clean(self):
        if self.following == self.followed_by:
            raise ValidationError(
                '<%s> cannot follow himself.' % self.user.username
            )

    def save(self, *args, **kwargs):
        self.clean()
        return super(Follow, self).save(*args, **kwargs)

    def __str__(self):
        return '<%s> is followed_by <%s>' % (
            self.following.username, self.followed_by.username)
