from django.contrib import admin
from .models import Menu, MenuItem

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'is_visible', )
    list_editable = ('is_visible', )
    list_filter = ('parent',)


admin.site.register(Menu)