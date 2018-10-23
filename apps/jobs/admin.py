from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username')
    search_fields = ('first_name', 'last_name', 'username')

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'budget', 'pay_type', 'length', 'created_at')
    search_fields = ('title', 'company', 'length', 'budget')
    date_hierarchy = 'created_at'

class UserAppliedAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'amount_charged', 'cover_letter')
    search_fields = ('job', 'user')
    raw_id_fields = ('job', 'user')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'slug', 'user', 'blog_category')
    search_fields = ('title', 'slug', 'user', 'blog_category')
    raw_id_fields = ('user', 'blog_category')
    date_hierarchy = 'created_at'

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

admin.site.register(User, UserAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(UserApplied, UserAppliedAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)