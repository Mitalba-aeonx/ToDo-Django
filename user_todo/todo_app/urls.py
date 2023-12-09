from django.contrib import admin
from django.urls import path
from todo_app import views

urlpatterns = [
    path('',views.home,name="home" ),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('add-todo/',views.add_todo,name="add_todo"),
    path('logout/',views.signout,name="logout"),
    path('delete-todo/<int:id>',views.delete_todo,name="delete_todo"),
    path('change-status/<int:id>/<str:is_completed>',views.update_status,name="delete_todo"),
    path('update-todo/<int:id>/',views.update_todo,name="update_todo"),

    


]
