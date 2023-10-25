from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=230
    )
    content = models.TextField()
    creation_date = models.DateTimeField(
        auto_now_add=True
    )
