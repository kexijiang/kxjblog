from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

import user
from comments.models import Comment

from articles.models import Articles
from sort.models import Sort, Article_sort


class IndexView(View):
    """首页"""

    def get(self, request):
        """显示首页"""
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
        #  判断是否登录
        if request.user.is_authenticated():
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
        # 获取该博客的所有评论
        comments = Comment.objects.filter(article=articles_id).order_by('-comment_date')
        if articles_id:
            article = Articles.objects.get(article_id=articles_id)
            # 组织上下文(传给页面的数据)
            context = {
                'comments': comments,
                'article': article,
                'sorts': sorts,
                'articles': articles,
                'hot_articles': hot_articles,
                'lately_articles': lately_articles,
                'sort_catalogues': sort_catalogues
            }
            article_views = int(article.article_views) + 1
            print(article_views)

            Articles.objects.filter(article_id=articles_id).update(article_views=article_views)
            return render(request, 'detail.html', context=context)
        else:
            return HttpResponse("文章不存在!")





class ArticlesListView(View):
    """博客list展示页面根据分类展示"""
    def get(self, request, sort_id):
        # 接收的参数 1.sort_id分类id
        # 业务处理 根据sort_id找到对应博文id
        print(sort_id)
        if sort_id:
            sort_id = int(sort_id)
            article_sort = Article_sort.objects.filter(sort_id=sort_id)
            article_ids = []
            for i in article_sort:
                print("博文id:"+str(i.article_id))
                article_ids.append(i.article_id)
            # 获取所有分类信息
            sorts = Sort.objects.all()
            # 获取该分类下所有博文信息
            articles = Articles.objects.filter(article_id__in=article_ids)
            print(articles)
            # 获取浏览量最高的9篇文章
            hot_articles = Articles.objects.order_by('-article_views')[:9]
            # 获取最近更新的文章
            lately_articles = Articles.objects.order_by('-article_date')[:9]
            # 获取所有分类
            sort_catalogues = Sort.objects.all()
            # 组织上下文(传给页面的数据)
            context = {'sorts': sorts,
                     'articles': articles,
                     'hot_articles': hot_articles,
                     'lately_articles': lately_articles,
                     'sort_catalogues': sort_catalogues
                     }
        return render(request, 'index.html', context=context)


class ArticlesSearchView(View):
    """博客list展示页面根据分类展示"""
    def post(self, request):
        # 接收的参数 1.sort_id分类id
        keyword = request.POST.get("keyword")
        # 业务处理 根据sort_id找到对应博文id
        print("搜索关键词为:"+keyword)
        if keyword:
            # 获取所有分类信息
            sorts = Sort.objects.all()
            # 根据博文简介模糊匹配
            articles = Articles.objects.filter(article_introduce__icontains=keyword)
            print(articles)
            # 获取浏览量最高的9篇文章
            hot_articles = Articles.objects.order_by('-article_views')[:9]
            # 获取最近更新的文章
            lately_articles = Articles.objects.order_by('-article_date')[:9]
            # 获取所有分类
            sort_catalogues = Sort.objects.all()
            # 组织上下文(传给页面的数据)
            context = {'sorts': sorts,
                     'articles': articles,
                     'hot_articles': hot_articles,
                     'lately_articles': lately_articles,
                     'sort_catalogues': sort_catalogues
                     }
        return render(request, 'index.html', context=context)