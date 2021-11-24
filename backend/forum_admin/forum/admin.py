from django.contrib import admin
from forum.models import ForumUser
class ForumUserAdmin(admin.ModelAdmin):
    fields = ('name', 'humor', 'tag')

admin.site.register(ForumUser, ForumUserAdmin)