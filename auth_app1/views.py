from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signupview(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, "auth_app1/sign.html", {"form": form})


def loginview(request):
    if request.method == "POST":
        u = request.POST.get('name')
        p = request.POST.get('pass')

        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('show')



    return render(request, "auth_app1/login.html", {})


def logoutview(request):
    logout(request)
    return redirect("login")

