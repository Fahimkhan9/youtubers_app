from django.contrib import admin
from .models import Youtubers
from django.utils.html import format_html
# Register your models here.
class YtAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    list_display = ('id','myphoto', 'name','subs_count','is_featured','category')
    list_display_links = ('name','id')
    search_fields = ('name','category')
    list_filter = ('category','crew','camera_type')
    list_editable = ('is_featured',)


admin.site.register(Youtubers, YtAdmin)