from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            auth.login(request, user)
            return redirect('news')
        return render(request, "accounts/signup.html")

    return render(request, "accounts/signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('news')
        else:
            return render(request, 'accounts/errorpage.html')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('news')
