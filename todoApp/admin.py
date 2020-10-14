from django.contrib import admin

# Register your models here.
from todoApp.models import User, ToDo, Reply, Comment

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','mobileNumber','created_at']

admin.site.register(User,UserAdmin)

class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','end_date','created_at','updated_at']

admin.site.register(ToDo,ToDoAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['comment','reply','created_at']

admin.site.register(Reply,ReplyAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['todo','comment','created_at']

admin.site.register(Comment,CommentAdmin)

