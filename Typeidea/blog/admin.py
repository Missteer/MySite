from django.contrib import admin

# Register your models here.

from django.urls import reverse
from django.utils.html import format_html
from .models import Category,Post,Tag
from .adminforms import PostAdminForm
from Typeidea.custom_site import custom_site
from Typeidea.base_admin import BaseOwnerAdmin
from django.contrib.admin.models import LogEntry


#我们需要在分类页面直接编辑文章
#当然，这是一个伪需求。 因为这种内置（ inline ）的编辑相关内容的操作更适合字段较少的 Model
class PostInline(admin.TabularInline):
    fields = ('title','desc')
    extra = 1 #控制额外多几个
    model = Post

#@admin.register(Category)
@admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline,]
    list_display = ('name','status','is_nav','created_time','post_count')
    fields = ('name','status','is_nav',)
#fields 这个配置的 作用就是控制页面上要展示的字段。
    #post_count,自定义字段，挺好玩
    def post_count(self,obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'

    #话不多说，先来抽象出一个基类 BaseOwnerAdrnin， 这个类帮我们完成两件事 ：
    # 一是重写 save 方法，此时需要设置对象的 ow口er；
    # 二是重写 get_queryset 方法，让列表页在展示文章 或者分类时只能展示当前用户的数据。
    #下面save_model移动到了base_admin.py中了
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin, self).save_model(request,obj,form,change)
    def __str__(self):
        return self.name

#@admin.register(Tag)
@admin.register(Tag,site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name','status','created_time')
    fields = ('name','status','owner')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request,obj,form,change)
    def __str__(self):
        return self.name

class CategoryOwnerFilter(admin.SimpleListFilter):
    '''自定义过滤器只展示当前用户分类'''
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


#@admin.register(Post)
@admin.register(Post,site=custom_site)
class PostAdmin(BaseOwnerAdmin):

    form = PostAdminForm
    #list_display,它用来配置列表页面展示哪些字段
    list_display = (
        'title','category','status','created_time','operator','owner'
    )
    #用来配置哪些字段可以作为链接，点击它们，可以进入编辑页面
    list_display_links = []
    #：配置页面过滤器，需要通过哪些字段来过滤列表页
    #list_filter = ['category',]
    list_filter = [CategoryOwnerFilter]
    #：配置搜索字段。
    search_fields = ['title','category_name']
    #动作相关的配置，是否展示在顶部。
    actions_on_top = True
    #动作相关的配置，是否展示在底部。
    actions_on_bottom = True

    #编辑页面、
    #保存、编辑、编辑并新建按钮是否在顶部展示。
    save_on_top = True
    #exclude 可以指定哪些字段是不展示
    exclude = ('owner',)
    #fields 配置有两个作用，一个是限定要展示的字段，另外一个就是配置展示字段的顺序。
    #fields = (
        #     ('category','title'),
        #     'desc',
        #     'status',
        #     'content',
        #     'tag',
        # )
    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields':(
                ('title','category'),
                'status'
            ),
        }),
        ('内容',{
            'fields':('desc','content',)
        }),
        ('额外信息',{
            'classes':('collapse',),
            'fields':('tag',),
        })
    )
    filter_horizontal = ('tag',) #横向多对多
    #filter_vertical = ('tag',) #纵向多对多
    def operator(self,obj):
        return format_html(
            '<a href="()">编辑</a>',
            #reverse('admin:blog_post_change',args=(obj.id,))
            reverse('cus_admin:blog_post_change',args=(obj.id,))

        )
    operator.short_description = '操作'
    #下面注释移动到了base_admin.py中
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request,obj,form,change)
    #
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    def __str__(self):
        return self.category

    class Media:
        css = {
            'all':("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/"
                   "bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap/bundle.js',)


@admin.register(LogEntry,site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr','object_id','action_flag','user',
                    'change_message']
