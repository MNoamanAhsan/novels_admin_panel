from django.contrib import admin

from .models import Categoryn, Novels, Episode

from django.contrib.auth.models import Group, User


class EpisodeInLine(admin.TabularInline):
    model=Episode
    extra=1


class NovelAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther', 'category')   
    list_filter = ('category',)
    search_fields = ('title', 'auther')
    inlines = [EpisodeInLine]


admin.site.register(Categoryn)
admin.site.register(Novels, NovelAdmin)
admin.site.register(Episode)

admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.site_header = "📚 Novels Admin Panel"
admin.site.site_title = "Novels Admin"
admin.site.index_title = "Welcome to Novels Management"
