
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    return render(request,'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return render(request,'profile_page.html',{'user': request.user})  # Replace 'home' with the name of your home page URL
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        


        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

     
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('signup')

       
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken.")
            return redirect('signup')

        
        user = User.objects.create_user(username=username, email=email, password=password1,first_name=first_name, last_name=last_name)

        user.save()

       
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            return render(request,'profile_page.html')  # Replace 'home' with the name of your home page URL pattern

    return render(request, 'signup.html')


@login_required
def profile(request):
    user = request.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name
    }
    return render(request, 'profile_page.html', context)




def logout_view(request):
    logout(request)
    return redirect('home') 


