from django.shortcuts import render

# Create your views here.
from django.views import View

from articles.models import Articles
from sort.models import Sort


class IndexView(View):
    """首页"""

    def get(self, request):
        """显示首页"""
        user = None
        try:
            user = request.get('user')
        except Exception as e:
            print(e)
            user = 1
        # 获取所有分类
        sorts = Sort.objects.all()
        # 获取所有博文信息
        articles = Articles.objects.all()
        # 获取浏览量最高的9篇文章
        hot_articles = Articles.objects.order_by('-article_views')[:9]
        # 获取最近更新的文章
        lately_articles = Articles.objects.order_by('-article_date')[:9]
        # 获取所有分类
        sort_catalogues = Sort.objects.all()
        # 组织上下文(传给页面的数据)
        context = {'sorts': sorts,
                   'user': user,
                   'articles': articles,
                   'hot_articles': hot_articles,
                   'lately_articles': lately_articles,
                   'sort_catalogues': sort_catalogues
                   }
        return render(request, 'index.html', context=context)


class Index1View(View):
    """首页"""
    def get(self, request):
        """显示首页"""
        if request.user.is_authenticated():
            try:
                user = request.GET.get('userObjJson')
            except Exception as e:
                print(e)
            # 获取所有分类
            sorts = Sort.objects.all()
            # 获取所有博文信息
            articles = Articles.objects.all()
            # 获取浏览量最高的9篇文章
            hot_articles = Articles.objects.order_by('-article_views')[:9]
            # 获取最近更新的文章
            lately_articles = Articles.objects.order_by('-article_date')[:9]
            # 获取所有分类
            sort_catalogues = Sort.objects.all()
            # 组织上下文(传给页面的数据)
            context = {'sorts': sorts,
                       'user': user.model,
                       'articles': articles,
                       'hot_articles': hot_articles,
                       'lately_articles': lately_articles,
                       'sort_catalogues': sort_catalogues
                       }
            return render(request, 'index.html', context=context)


class ArticlesDetailView(View):
    """详细博客页面"""
    # 根据博客id进行查询
    def get(self, request, articles_id):
        return render(request, 'index.html')


class ArticlesListView(View):
    """博客list展示页面"""
    def get(self, request, sort_id):
        return render(request, 'index.html')