from django.urls import path
from . import views
from .views import edit_task

urlpatterns = [
    path('', views.task_list, name='task_list'),  # ✅ Now '/tasks/' works
    path('add/', views.add_task, name='add_task'),
    path('task/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('login/', views.login_user, name='login_user'),
    path('signup/', views.signup_user, name='signup_user'),
    path('logout/', views.logout_user, name='logout_user'),
]
