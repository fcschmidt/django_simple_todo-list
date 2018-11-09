from django.db import models


class TodoItem(models.Model):
    item = models.TextField()

    def __str__(self):
        return self.item
