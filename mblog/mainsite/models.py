from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    #title 用来显示文章标题
    title = models.CharField(max_length=200)
    #slug 文章的网址
    slug = models.CharField(max_length=200)
    #body是文章内容
    body = models.TextField()
    #文章发表时间
    pub_date = models.DateTimeField(default=timezone.now)
    #class Meta内的设置则要指定文章显示的顺序是以pub_date为依据
    class Meta:
        #pub_date 我们以timezone的方式让他自动产生
        ordering = ('-pub_date',)

    # def __unicode__(self):
    #     return self.title

    def __str__(self):
        return self.title