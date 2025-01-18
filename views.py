from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Contact
def my_view(request):
    return render(request, 'base.html',{'check_signup':"signup"})
def check_registration(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('re_enter_password'):
            i_name = request.POST.get('name')
            i_phone_number = request.POST.get('phone_number')
            i_email = request.POST.get('email')
            i_pass = request.POST.get('password')

            if User.objects.filter(phone_no=i_phone_number).exists() or User.objects.filter(email=i_email).exists():
                return render(request, "base.html", {'error_message': 'Phone number or email is already registered','check_signup':"signup"})

            if i_name and i_phone_number and i_email and i_pass:
                user = User(name=i_name, phone_no=i_phone_number, email=i_email, password=i_pass)
                user.save()
                return render(request, 'base.html', {'success_message': 'User added successfully!','check_signup':"signup"})
            else:
                return render(request, 'base.html', {'error_message': 'All fields are required. Please try again.','check_signup':"signup"})

        else:
            return render(request, "base.html", {'error_message': 'Passwords do not match','check_signup':"signup"})

    return render(request, 'base.html',{'check_signup':"signup"})  
def check_login(request):
    return render(request, 'base.html',{'check_login':"login"})



def signing_in(request):
    if request.method=='POST':
        i_email=request.POST.get('email')
        i_pass=request.POST.get('password')
        if  User.objects.filter(email=i_email).exists():
            user = User.objects.get(email=i_email)
            contacts =Contact.objects.filter(user=user)
            print(contacts,user.name)
            return render(request, 'user.html', {'success_message': 'Login successfully!','user':user.name,'data':contacts})
        else:
            return render(request,'base.html',{'check_login':"login",'error_message':"log does not exists"})
    
    return render(request,'base.html',{'check_login':"login",'error_message':"try again"})

