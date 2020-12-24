from django.db import models
from posts.models import Post
from django.conf import settings

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    like = models.BooleanField(default=False)
