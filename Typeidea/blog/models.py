from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    #类别
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS =(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )

    name = models.CharField(max_length=50,verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,
                                         verbose_name="状态")
    is_nav = models.BooleanField(default=False,verbose_name="是否为导航")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    @classmethod
    def get_navs(cls):
        '''得到分类是否是导航'''
        categories = cls.objects.filter(status=cls.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                '''是导航的分类'''
                nav_categories.append(cate)
            else:
                '''不是导航的分类'''
                normal_categories.append(cate)
        return {
            'navs':nav_categories,
            'categories':normal_categories,
        }




class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除')
    )

    name = models.CharField(max_length=10,verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,verbose_name="状态")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):

    STAUTS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STAUTS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
        (STATUS_DRAFT,'草稿'),
    )

    title = models.CharField(max_length=255,verbose_name="标题")
    desc = models.CharField(max_length=1024,blank=True,verbose_name="摘要")
    content = models.TextField(verbose_name="正文",help_text="正文必须是markdown格式")
    status = models.PositiveIntegerField(default=STAUTS_NORMAL,
                                         choices=STATUS_ITEMS,verbose_name="状态")
    category = models.ForeignKey(Category,verbose_name="分类",on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,verbose_name="标签")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)


    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id'] #根据id进行降序排列


    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)\
                .select_related('owner', 'category')
        return post_list, tag


    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(status=Post.STAUTS_NORMAL)\
                .select_related('owner', 'category')

        return post_list, category

    @classmethod
    def latest_posts(cls):
        return cls.objects.filter(status=cls.STAUTS_NORMAL)
        # posts = Post.objects.all()
        # queryset = posts.filter(status=1)
        #return queryset
    @classmethod
    def hot_posts(cls):

        '''最热文章'''
        '''only，只获取 title,category 的内容， 其他值在获取时会产生额外的查'''
        return cls.objects.filter(status=cls.STAUTS_NORMAL).order_by('-pv').only('title','category')


