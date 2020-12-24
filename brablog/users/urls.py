from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    # path() для страницы регистрации нового пользователя
    # её полный адрес будет auth/signup/, но префикс auth/ обрабатывется в головном urls.py
    path("signup/", views.sign, name="signup"),
    path("logout", views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]