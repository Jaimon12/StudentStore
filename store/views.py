from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate, login as django_login
# Create your views here.
def register(request):  
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username had allready Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save(); 
            return redirect('login')
        else:
            messages.info(request,"passwoerd not maching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            django_login(request, user)
            return redirect('courses')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')

# @login_required
def logout(request):
    django_logout(request)
    return redirect('index') 
# @login_required
def index(request):
    return render(request, 'index.html', {'user': request.user})


def course(request):
    return render(request, 'courses.html')
def information_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        age =  request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        phone_number = request.POST.get('phone_number', '')
        mail_id = request.POST.get('mail_id', '')
        address = request.POST.get('address', '')
        department = request.POST.get('department', '')
        course = request.POST.get('course', '')
        purpose = request.POST.get('purpose', '') 
        materials_provide = request.POST.get('materials_provide', '')
        return redirect('success_page', purpose=purpose)  # Pass required parameters here
    return render(request, 'form.html')

def success_page(request, purpose):
    message = f"Order Confirmed for: {purpose}"  # Modify the message to include the purpose
    return render(request, 'success.html', {'message': message})