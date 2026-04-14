from django.shortcuts import render, redirect
from django.contrib import messages # <--- Add this import
from .forms import FaultForm

def reportform(request):
    if request.method == 'POST':
        form = FaultForm(request.POST)
        if form.is_valid():
            new_fault = form.save()
            new_fault.refresh_from_db()
            return redirect('status_page')
        # If form is NOT valid, it falls through to the render below
    else:
        # This handles the initial GET request (the first time they visit the page)
        form = FaultForm()

    # CRITICAL: This return must be at the very bottom, outside all if/else blocks
    return render(request, 'reports/report_form.html', {'form': form})