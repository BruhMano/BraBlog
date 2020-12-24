from django.db import models

class Group(models.Model):
    title = models.TextField(max_length=20)
    slug = models.SlugField()
    desc = models.TextField()
    def __str__(self):
        return self.title