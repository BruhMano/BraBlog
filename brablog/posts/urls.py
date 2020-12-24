from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("fav", views.fav, name="fav"),
    path("post/<str:postname>/", views.post, name="post"),
    path("newpost/", views.newpost, name="newpost"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)