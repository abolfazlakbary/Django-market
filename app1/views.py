from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from app1.models import Article, ArticleCatagory

@login_required(login_url='login')
def home(request):
    articles = Article.objects.all()
    categories = ArticleCatagory.objects.all()
    context={
        'articles':articles ,
        'categories':categories ,
    }
    return render(request, 'home.html', context)

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']
            if password == password_confirmation:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.set_password(password)
                    user.save()
                    return redirect('home')
            else:
                messages.info(request, 'Passwords are not match')
                return redirect('register')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Invalid username or password')
                return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('login')

def selected_category(request, selected_category):
    thecategory = None
    articles = Article.objects.all()
    categories = ArticleCatagory.objects.all()
    if selected_category is not None:
        thecategory = ArticleCatagory.objects.get(category=selected_category)
    thearticle = Article.objects.filter(category=thecategory)
    context = {
        'articles':articles ,
        'categories':categories ,
        'thecategory':thecategory ,
        'thearticle':thearticle ,
    }
    return render(request, 'categories.html', context)

