from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def register(request):
    if request.method== 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, find your job today!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def custom_logout(request):
    logout(request)
    # Redirect to a specific page after logout (optional)
    return HttpResponseRedirect(reverse('index'))