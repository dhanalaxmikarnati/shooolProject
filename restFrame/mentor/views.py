from django.shortcuts import render
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(request,user)
         
          return redirect("/")
        else:
           messages.info(request,"invalid credentials.....")
           return redirect('login')
    else:
      
      return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if(password1==password2):
             if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('register')
             elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
             else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                #print('user created')
                return redirect('login')
        else:
             messages.info(request,'password not matching.....')
             return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
   auth.logout(request)
   return redirect('/')         