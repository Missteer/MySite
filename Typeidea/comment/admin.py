from django.contrib import admin

# Register your models here.
from .models import Comment
from Typeidea.custom_site import custom_site
from Typeidea.base_admin import BaseOwnerAdmin

#@admin.register(Comment)
@admin.register(Comment,site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'target','nickname','website','email','created_time',
        'status',
    ]

    list_filter = [
        'nickname','content','target'
    ]

    search_fields = ['nickname','content']

    def __str__(self):
        return self.target
