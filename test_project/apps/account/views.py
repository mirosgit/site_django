from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth


def index(request):
    return render(request, 'base.html')


def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Данный email уже зарегистрирован')
        else:
            if form.is_valid():

                ins = form.save()
                password = form.cleaned_data['password1']

                user = authenticate(password=password, username=email, email=email)
                ins.email = email
                ins.save()
                form.save_m2m()
                messages.success(request, 'Вы успешно зарегестрировались ')
                return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'account/register.html',  {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')














