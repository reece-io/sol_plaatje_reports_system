from django.shortcuts import render
from reports.models import Fault

def home(request):
    # A simple landing page
    return render(request, 'dashboard/home.html')

def status_page(request):
    # Fetch all faults from the database, newest first
    faults = Fault.objects.all().order_by('-created_at')
    return render(request, 'dashboard/status_page.html', {'faults': faults})