from django.contrib import admin

# Register your models here.
from .models import Link,SideBar
from Typeidea.custom_site import custom_site
from Typeidea.base_admin import BaseOwnerAdmin

#@admin.register(Link)
@admin.register(Link,site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = (
        'title','href','status','weight','created_time'
    )
    fields = (
        'title','href','status','weight'
    )
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(LinkAdmin, self).save_model(request,obj,form,change)

    def __str__(self):
        return self.title


#@admin.register(SideBar)
@admin.register(SideBar,site=custom_site)
class SideBarAdmin(admin.ModelAdmin):
    list_display = [
        'title','display_type','content','created_time','status'
    ]

    fields = ['title','display_type','content',]
    list_filter = ['title']