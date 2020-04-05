from django.contrib import messages
from django.shortcuts import render,redirect
from app24.models import EmployeeModel


def showIndex(request):
    qs = EmployeeModel.objects.all()
    return render(request,"index.html",{"data":qs})


def saveEmployee(request):
    if request.method == "POST":
        # idno = request.POST["t1"]
        name = request.POST["t2"]
        img = request.FILES["t3"]
        EmployeeModel(name=name,photo=img).save()
        #return render(request,"index.html",{"message":"Data Saved"})
        messages.success(request,"Employee Details are saved")
        #return redirect('main')
    else:
        return showIndex(request)