import re

from django.contrib.auth import login
from django.core.serializers import serialize
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import View

from user.models import User


class RegisterView(View):
    """注册"""
    """显示注册页面"""
    def get(self, request):
        return render(request, 'register.html' )
    """注册处理逻辑"""
    def post(self, request):
        # 1.接收数据
        # 2.校验数据
        # 3.业务处理
        # 4.返回应答
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # 进行数据校验
        print([username, password, email])
        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})
        # 校验邮箱格式
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
        # 校验用户名是否存在
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})
        # 进行业务处理：
        user = User()
        user.set_password(password)
        user.username = username
        user.password = password
        user.email = email
        user.is_active = 1  # 设置账户状态 未进行激活
        user.save()
        return redirect(reverse('articles:index'),request)


class LoginView(View):
    """登录"""
    """显示登录页面"""
    def get(self, request):
        return render(request, 'login.html')
    """登录处理逻辑"""
    def post(self, request):
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username+";"+password)
        # 判断用户名密码是否存在
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})
        # user1 = authenticate(username=username,password=password)
        # user = User.objects.get(username=username)
        search_dict = dict()
        search_dict['username'] = username
        search_dict['password'] = password
        user = User.objects.filter(**search_dict).first()
        print(user)
        print("username=" + username + ";password=" + password)
        # 业务处理，登录经验
        if user is not None:
            # 账户是否激活
            if user.is_active:
                print("用户已激活")
                # 系统的登录方法，会将登录id放入session
                login(request, user)
                return redirect(reverse('articles:index'))
        # if user is None:
        #     search_dict = dict()
        #     search_dict['user_email'] = username
        #     search_dict['user_password'] = password
        #     user = User.objects.filter(**search_dict).first()
        #     print("user="+user)
        #     if user is None:
        #         print('无此用户!')  # 后期修改为ajax方式给前端页面提示
        else:
            return render(request, 'login.html', {'errmsg': '用户名密码错误'})
