"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('cbvlist/', views.TaskListView.as_view(),name='cbvlist'),
    path('delete/<int:id1>/', views.delete,name='delete'),
    path('update/<int:id2>/', views.update,name='update'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(),name='cbvdelete'),
]
