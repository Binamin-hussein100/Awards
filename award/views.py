from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .forms import PostForm
from django.http import HttpResponseRedirect
from .models import Project

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password2')
        
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.warning(request, 'Username already exists. Try another')
                return redirect('register')
            else:
               if User.objects.filter(email = email).exists():
                   messages.warning(request, 'Email already exists. Try another')
                   return redirect('register')
               else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    return redirect('login')
        else:
            messages.warning(request, 'Password must match.')
            return redirect('register')
    else:
        return render(request,'register.html')
                
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username,password = password)
        
        if user is not None:
            auth.login(request,user)
            messages.info(request, 'Log in successful.')
            
            return redirect('home')
        else:
            messages.warning(request, 'Save was successful.')
            return redirect('login')
    else:
        return render(request,'login.html')
        
def index(request):
    projects = Project.objects.all()
    return render(request,'post.html',{"projects":projects})

def prj_form(request):
    if request.method=='POST':
        myForm = PostForm(request.POST,request.FILES)
        if myForm.is_valid():
            myForm.save()
            return HttpResponseRedirect('/')
        
    else:
        myForm = PostForm()
    return render(request,'homeprj.html',{"myForm":myForm})

def search(request):
    if request.method=='GET':
        query = request.GET.get('q')
        if query:
            searched = Project.objects.filter(title__icontains=query)
            return render(request,'searched.html',{'searched':searched})
              