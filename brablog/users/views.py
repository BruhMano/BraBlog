from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login") #  где login — это параметр "name" в path()
    template_name = "signup.html"

def sign(request):
    form = CreationForm
    if request.method == "POST":
        form = CreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect(reverse_lazy("login"))
        else:
          form = CreationForm()

    return render(request, 'signup.html', locals())

def logout(request):
    logout(request)