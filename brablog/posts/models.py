from django.db import models
from django.contrib.auth import get_user_model
from groups.models import Group
User = get_user_model()
group = Group()

class Post(models.Model):
    title = models.TextField(max_length=150)
    text = models.TextField()
    pub_date = models.DateField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(blank=True,null = True,upload_to = "media")
    is_liked_by_current_user = models.BooleanField()
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.title 
