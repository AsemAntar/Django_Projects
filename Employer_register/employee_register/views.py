from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)


def employee_form(request, id=0):
    if request.method == 'POST':
        if id == 0:
            form = EmployeeForm(data=request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(data=request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')
    else:
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html', {'form': form})


def delete_employee(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')
