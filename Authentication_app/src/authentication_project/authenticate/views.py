from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm
from .models import Signup
from django.contrib.auth import  authenticate, login
from django.contrib.auth.hashers import check_password, make_password  

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')
        print(username, email, password1, password2)
        if password1==password2:
            hashed_password=make_password(password1)
            Signup.objects.create(username=username, email=email, password1=hashed_password)
            return redirect('login')
        else: 
            form.errors()
    else:
        form = SignupForm()

    context = {
        "form": form
    }
    return render(request, "signup.html", context)

# def login_view(request):
#     if request.method == 'POST': 
#         email=request.POST.get("email")
#         pass1=request.POST.get("password")
#         user=authenticate(request, email=email, password1=pass1)
#         print(user)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#     return render(request, "login.html", {})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = Signup.objects.get(username=username)
        print(Signup.objects.get(username=username ))
        if password==user.password1:
            login(request, user)
            return redirect('home')
    return render(request, "login.html", {})

def home_view(request):
    return render(request, "home.html", {})