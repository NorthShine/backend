from django.db import models


class PersistentMessage(models.Model):
    recipient = models.TextField()
    message = models.TextField()
    author = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
