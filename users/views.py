from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.urls import reverse
# Create your views here.


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
    
    def clean(self):
        clean_data = super().clean()
        password = clean_data.get("password")
        confirm_password = clean_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password not match.")
        


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
    
        if form.is_valid():
            user = form.save(commit=False)  # user is an object of form and not commit to sql
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            messages.success(request, "Successfully register")

            return HttpResponseRedirect(reverse("users:login"))
        
    else:
        form = RegisterForm()
    
    return render(request, "users/register.html",{
        "form" : form
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]  # like a dict, "username" as a key and its value is a str
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("tasks:task_list"))
        else:
            #messages.error(request, "Invalid name or password")
            return render(request, "users/login.html", {
                "message": "Invalid name or password."
            })
        
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logout")
    return render(request, "users/welcome.html")


def welcome(request):
    return render(request, "users/welcome.html")