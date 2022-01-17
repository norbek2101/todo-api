from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    target = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    choice_color = [
        ('red', 'Do it now'),
        ('orange', 'Must do today'),
        ('yellow', 'Do it anyway'),
        ('blue', 'Do it'),
        ('green', 'Just do it'), 
    ]
    type  = models.CharField(
        max_length=11,
        choices= choice_color,
        default='green',
    )

    def __str__(self):
        return  self.target + '---targeted_by: ' + str(self.user).upper()

     