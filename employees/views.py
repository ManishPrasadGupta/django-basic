from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Employee


# Create your views here.
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    context = {
        'employee': employee
    }
    return render(request, 'employee_detail.html', context)