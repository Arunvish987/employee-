from django.shortcuts import render, redirect
from .forms import EmployeeForm
from . models import Employee

# Create your views here.

def employee_list(request):
    context = {'employee_list' : Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)

def employee_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html',{'form':form})

    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employee_list')

def employee_update(request, pk):

        employee = Employee.objects.get(id=pk)
        form = EmployeeForm(instance=employee)
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                return redirect('employee_list')

        return render(request, 'employee_register/employee_form.html', {'form': form})





