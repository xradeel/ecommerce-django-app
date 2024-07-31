from django.contrib import admin
from .models import Banner_feature
# Register your models here.
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ('title', 'updatedat')

from django.utils.html import format_html

class BannerAdmin(admin.ModelAdmin):

    def icon(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    icon.short_description = 'Image'
    list_display = ['title', 'icon',]


admin.site.register(Banner_feature, BannerAdmin)