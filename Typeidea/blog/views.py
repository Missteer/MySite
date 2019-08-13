from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Post,Tag,Category
from config.models import SideBar


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context

# class IndexView(CommonViewMixin,ListView):
#     queryset = Post.latest_posts()
#     paginate_by = 5
#     context_object_name = 'post_list'
#     template_name = 'blog/list.html'

class PostDetailView(DetailView):
    model = Post
    paginate_by = 1
    template_name = 'blog/detail.html'
    #context_object_name拿到要渲染到模板中的这个queryset名称
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'



class IndexView(CommonViewMixin,ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    # context_object_name拿到要渲染到模板中的这个queryset名称
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    '''有两个方法需要重写： 一个是 get_context_data 方法，用来获取上下文数据－并最终将其传入模板；
     另外一个是 get_queryset 方法，用来获取 指定 Model 或 QuerySet 的数据'''
    def get_context_data(self, **kwargs):

        context = super(CategoryView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category,pk=category_id)
        context.update({
            'category':category
        })
        return context


    def get_queryset(self):
        '''重写queryset,根据分类过滤'''
        queryset = super(CategoryView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag,pk=tag_id)
        context.update({
            'tag':tag
        })
        return context

    def get_queryset(self):
        queryset = super(TagView, self).get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)

# def post_list(request,category_id=None,tag_id=None):
#     tag = None
#     category = None
#     if tag_id:
#         post_list,tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         post_list,category = Post.get_by_category(category_id)
#
#     else:
#         post_list = Post.latest_posts()
#
#     context = {
#         'category':category,
#         'tag':tag,
#         'post_list':post_list,
#         'sidebars':SideBar.get_all(),
#     }
#     context.update(Category.get_navs())
#     return render(request,'blog/list.html',context=context)




# def post_detail(request,post_id=None):
#     try:
#         post = Post.objects.get(id=post_id)
#         print(type(post))
#     except Post.DoesNotExist:
#         post = None
#     context={
#         'post':post
#     }
#     context.update(Category.get_navs())
#     return render(request,'blog/detail.html',context=context)
class  SearchView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data()
        context.update(
            {
                'keyword':self.request.GET.get('keyword','')
            }
        )
        return context

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))


class AuthorView(IndexView):
    '''增加作者页面'''
    def get_queryset(self):
        queryset = super(AuthorView, self).get_queryset()
        author_Id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_Id)














