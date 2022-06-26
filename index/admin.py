from multiprocessing.connection import Client

from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import About, Category, Client, Slider


class SliderAdmin(admin.ModelAdmin):
    readonly_fields = ['old_image']
    list_display = ('title', 'Description', 'Image',
                    'is_deleted', 'action', 'extra_title')
    list_display_links = ('title', 'Description', 'Image')
    list_filter = ['title', 'is_deleted', 'created_at',
                   ('extra_title', admin.EmptyFieldListFilter)]
    radio_fields = {"color": admin.VERTICAL}
    list_per_page = 10

    def Description(self, obj):
        return obj.description[:150], '...'

    def Image(self, obj):
        return format_html(f"<img src='{obj.image.url}' width='200' />")

    def action(self, obj):
        return format_html(f"<a href='/admin/index/slider/{obj.id}/change/'>View</a>")

    def old_image(self, obj):
        return format_html(f"<img src='{obj.image.url}' width='200' />")


class AboutAdmin(admin.ModelAdmin):
    site_header = "About Settings"

    def has_add_permission(self, obj):
        if About.objects.all().count() >= 1:
            return False
        else:
            return True


admin.site.register(About, AboutAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Client)
admin.site.register(Category)
