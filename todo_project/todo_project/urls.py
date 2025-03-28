from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ✅ Import redirect function
from taskade import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ✅ Redirect root URL `/` to `/tasks/`
    path('', lambda request: redirect('task_list'), name='home'),  

    # ✅ Task-related routes
    path('tasks/', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # ✅ Authentication routes
    path('login/', views.login_user, name='login'), 
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
]
