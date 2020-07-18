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
        pass


class LoginView(View):
    """登录"""
    """显示登录页面"""
    def get(self, request):
        return render(request, 'login.html')
    """登录处理逻辑"""
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username, password]):
            print('登录出错!')
        print(username, password)
        search_dict = dict()
        search_dict['user_name'] = username
        search_dict['user_password'] = password
        user = User.objects.filter(**search_dict).first()
        print("user=" + str(user.user_id))
        sqlOrder = get_object_or_404(User, user_name=username)
        userObjJson = serialize('json', [sqlOrder])[1:-1]
        print(userObjJson)
        # if user is None:
        #     search_dict = dict()
        #     search_dict['user_email'] = username
        #     search_dict['user_password'] = password
        #     user = User.objects.filter(**search_dict).first()
        #     print("user="+user)
        #     if user is None:
        #         print('无此用户!')  # 后期修改为ajax方式给前端页面提示
        return redirect(reverse('articles:index1', userObjJson))
