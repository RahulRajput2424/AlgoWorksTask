from django.contrib import admin
from django.urls import path, include
from todoApp.views import UserSignupView, UserLoginView, AddTodoView, EditToDoView, DeleteToDoView,ToDoListView,\
    AddComment,AddReply,AdminToDoListView

urlpatterns = [
    path('user_signup_view/',UserSignupView.as_view()),
    path('user_login_view/', UserLoginView.as_view()),
    path('add_todo/', AddTodoView.as_view()),
    path('edit_todo/<int:pk>/', EditToDoView.as_view()),
    path('delete_todo/<int:pk>/', DeleteToDoView.as_view()),
    path('todo_list/', ToDoListView.as_view()),
    path('add_comment/<int:pk>/', AddComment.as_view()),
    path('add_reply/<int:pk>/', AddReply.as_view()),
    path('admin_todo_list/', AdminToDoListView.as_view()),
]








