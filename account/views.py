from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request,user)
                return HttpResponse('欢迎你，您已经成功登录!')
            else:
                return HttpResponse('登录失败！')
    else:
        login_form = LoginForm()
        return render(request,'account/login.html',{'form':login_form})

def user_profile(request):
    return render(request,'account/success.html')

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            #可以引导到登陆页
            return HttpResponse("你已经成功注册")
        else:
            return HttpResponse('对不起，你不能注册！')
    else:
        user_form = RegistrationForm()
        return render(request,'account/register.html',{'form':user_form})
