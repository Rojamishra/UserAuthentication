from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,SetPasswordForm
from app1.forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def index(request):
    context = {'msg': 'This is project main page','user':request.user}
    return render(request,'app1/index.html',context)

def users(request):
    context = {'msg': 'This is users main page'}
    return render(request,'app1/index.html',context)

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully')
            form = SignupForm()
    else:
        form = SignupForm()
    context = {'form':form}
    return render(request,'app1/signup.html',context)

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=uname,password=pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Done Successfully!!!')
                    return HttpResponseRedirect('/app1/profile')
        else:
            form = AuthenticationForm
        context = {'form':form,'msg':'This is Login page'}
        return render(request,'app1/log_in.html',context)
    else:
        return HttpResponseRedirect('/app1/profile')

def profile(request):
    if request.user.is_authenticated:
        context = {'msg':'This is {} profile page'.format(request.user),'user':request.user}
        return render(request,'app1/profile.html',context)
    else:
        return HttpResponseRedirect('/app1/login')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/app1/login')

#change pwd after login if you know the old password
def changepwd1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'pwd changed successfully !!')
                return HttpResponseRedirect('/app1/profile')
        else:
            form = PasswordChangeForm(user=request.user)
        context={'msg':'change password1 page','form':form}
        return render(request,'app1/changepwd1.html',context)
    else:
        return HttpResponseRedirect('/app1/login')
    
    
#change pwd after login if you forgot the old password
def changepwd2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'pwd changed successfully !!')
                return HttpResponseRedirect('/app1/profile')
        else:
            form = SetPasswordForm(user=request.user)
        context={'msg':'change password1 page','form':form}
        return render(request,'app1/changepwd1.html',context)
    else:
        return HttpResponseRedirect('/app1/login')