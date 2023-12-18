from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import UserProfile
from django.contrib import auth
from django.contrib.auth.models import User 
from django.contrib import messages
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
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('courses')
        else:
            messages.info(request,"Invalid Canidate")
            return redirect('login')

    return render(request,'login.html')
def Logout(request):
    auth.logout(request)
    return redirect('/')
def index(request):
    return render(request, 'index.html')


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
        return redirect('success_page',name=name,dob=dob,age=age,gender=gender,phone_number=phone_number,mail_id=mail_id,address=address,department=department,course=course, purpose=purpose,materials_provide=materials_provide)
    return render(request, 'form.html')

def success_page(request, purpose):
    message = f"Order Confirmed for: {purpose}"  # Modify the message to include the purpose
    return render(request, 'success.html', {'message': message})