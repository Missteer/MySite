from django.contrib import admin

# Register your models here.
from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'target','nickname','website','email','created_time',
        'status'
    ]

    list_filter = [
        'nickname','content','target'
    ]

    search_fields = ['nickname','content']

    def __str__(self):
        return self.target
