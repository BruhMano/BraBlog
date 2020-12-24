from django.urls import path

from . import views

urlpatterns = [
    path("add/<str:poste>/<str:usere>/",views.like_add, name="lake")
]