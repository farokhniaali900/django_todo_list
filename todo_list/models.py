from django.db import models

class todo_objects(models.Model):
    title = models.CharField(
        max_length=50,
    )
    task = models.TextField(
        max_length=200,
    )
    done = models.BooleanField(
        default=False
    )
