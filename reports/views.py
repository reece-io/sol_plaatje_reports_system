from django.shortcuts import render, redirect
from django.contrib import messages # <--- Add this import
from .forms import FaultForm

def reportform(request):
    if request.method == 'POST':
        form = FaultForm(request.POST)
        if form.is_valid():
            form.save()
            # Add the success message here
            messages.success(request, 'Your fault report has been successfully submitted to the Municipality!')
            return redirect('status_page')
    else:
        form = FaultForm()
    return render(request, 'reports/report_form.html', {'form': form})