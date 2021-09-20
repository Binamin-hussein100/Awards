from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.warning(request, 'Username already exists. Try another')
                return redirect('register')
            else:
               if User.objects.filter(email = email).exists():
                   messages.warning(request, 'Email already exists. Try another')
                   return redirect('register')
               else:
                    user = User.objects.create_user(username=username,password=password)
                    user.save()
                    messages.INFO(request, 'Save was successful.')
                    return redirect('login')
        else:
            messages.warning(request, 'Password must match.')
            return redirect('register')
    else:
        return render(request,'register.html')
                
def login(request):
    pass