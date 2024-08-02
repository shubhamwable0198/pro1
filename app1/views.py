from django.shortcuts import redirect, render
from .forms import EmployeeForm
from . models import Employee
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def addview(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render(request, "app1/add.html", {"form": form})


def showview(request):
    obj = Employee.objects.all()

    return render(request, "app1/show.html", {"obj": obj})


@login_required(login_url="login")
def updateview(request, pk):
    
    obj = Employee.objects.get(eid=pk)
    form = EmployeeForm(instance=obj)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show")

    return render(request, "app1/add.html", {"form": form})


@login_required(login_url="login")
def deleteview(request, pk):
    obj = Employee.objects.get(eid=pk)
    obj.delete()
    return redirect('show')
