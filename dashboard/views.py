from django.shortcuts import render
from reports.models import Fault
from django.contrib import messages


def reportform(request):
    if request.method == 'POST':
        form = FaultForm(request.POST)
        if form.is_valid():
            new_fault = form.save() 
            # This line forces Django to re-read the Ref # and Date from the DB
            new_fault.refresh_from_db() 
            return redirect('status_page')

def home(request):
    return render(request, 'dashboard/home.html')

def status_page(request):
    faults = Fault.objects.all()
    return render(request, 'dashboard/status_page.html', {'reported_faults': faults})

def report_fault(request):
    if request.method == 'POST':
        form = FaultForm(request.POST)
        if form.is_view():
            new_fault = form.save()
            new_fault.refresh_from_db() # This pulls the new Ref # from the database
            messages.success(request, f"Fault logged! Ref: {new_fault.ref_number}")
            return redirect('status_page')