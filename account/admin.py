from django.contrib import admin
from .models import Post, UserProfile, FeaturedPost, ReviewPost, Message, DailyReview

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class FeaturedAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)
admin.site.register(DailyReview)
admin.site.register(FeaturedPost, FeaturedAdmin)
admin.site.register(ReviewPost)
admin.site.register(Message)


