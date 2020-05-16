from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        un = request.POST['uname']
        pass1 = request.POST['pass']
        user = auth.authenticate(username=un, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid login credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        un = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=un).exists() or User.objects.filter(email=email).exists():
                messages.info(request, "username / email taken")
            else:
                user = User.objects.create_user(username=un, password=pass1, email=email, first_name=fn, last_name=ln)
                user.save()
                messages.success(request, "user created")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')
