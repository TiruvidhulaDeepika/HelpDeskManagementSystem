from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.
@login_required(login_url='loginpage')
def index(request):
    return render(request, "app/home.html")

def register(request):
    return render(request, "app/register.html")

def loginpage(request):
    return render(request, "app/login.html")

@login_required(login_url='loginpage')
def Raised(request):
    return render(request, "app/raise_ticket.html")

@login_required(login_url='loginpage')
def success(request):
    return render(request, "app/success.html")

@login_required(login_url='loginpage')
def showuser(request):
    return render(request, "app/show_user.html")

@login_required(login_url='loginpage')
def faq(request):
    return render(request, "app/faq.html")

def registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create(
            username=username,
            email=email,
        )
        new_user.set_password(password)
        new_user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('loginpage')

    return render(request, 'app/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        elif request.user.is_authenticated:
            return redirect("loginpage")
        else:
            messages.success(request, "error credentials")
            return render(request, 'app/login.html')
    else:
        return render(request, 'app/login.html')
    
@login_required(login_url='loginpage')
def raise_ticket(request):
    if request.method == 'POST':
        issue = request.POST.get('issue')
        title = request.POST.get('title')
        user = request.user
    
        new_query = raiseticket.objects.create(
            issue=issue, 
            title=title,
            user=user
        )

        return redirect("success")
    else:
        return render(request, 'app/raise_ticket.html')
    
@login_required(login_url='loginpage')
def show(request):
    show_data = raiseticket.objects.all()
    return render(request, "app/show_user.html", {"show_data": show_data})

@login_required(login_url='loginpage')
def Detailed(request, pk):
    new_data = get_object_or_404(raiseticket, pk=pk)
    return render(request, "app/detailed.html", {"new_data": new_data})

@login_required(login_url='loginpage')
def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("loginpage")
    
