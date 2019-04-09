from django.contrib import admin
from .models import Post,Product
# Register your models here.

#admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','pub_date']

admin.site.register(Post,PostAdmin)

admin.site.register(Product)