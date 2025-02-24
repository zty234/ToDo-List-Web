from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # make sure every user can only see their own tasks
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) # auto record created time
    due_date = models.DateTimeField(null=True, blank=True)  # could type ddl


    def __str__(self):
        return self.content

