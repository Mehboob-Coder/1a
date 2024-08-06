from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.
def thank(request):
    return render(request,'a1.html')


from django.contrib import messages

def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
         
            # Form is valid, process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            reg=user(name=name,email=email,password=password)
            reg.save()
            # reg.delete()
            
            # Save the data to the database or perform any other action
            messages.success(request, 'Registration successful!')
            
            # return HttpResponseRedirect('/a1/')
    else:
        form = StudentForm()
    
    return render(request, 'show_regestration.html', {'form': form})