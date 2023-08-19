from django.shortcuts import render, redirect
import datetime
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def loginview(request):
        if request.method == 'POST':
             form = AuthenticationForm(request, request.POST)
             if form.is_valid():
                  username = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')
                  user = authenticate(username=username, password=password)
                  if user is not None:
                       login(request, user)
                       return redirect('/')
                  else:
                       messages.error(request, 'Invalid Username or Password')
        else:
             form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
        
def logoutview(request):
    logout(request)
    return redirect('login')


@login_required
def edit_profile(request):
    if request.method == "POST":
         form = PasswordChangeForm(request.user, request.POST)
         if form.is_valid():
              user = form.save()
              update_session_auth_hash(request, user)
              messages.success(request, "Reset Success")
              return redirect('/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'edituser.html', {'form': form})