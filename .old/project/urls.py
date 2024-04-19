"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include # Importar 'include' para os path

# Importar as classes da views
from curriculum42.views import UserNew, UserList, UserUpdate, UserDetail, UserDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adicionar arquivo de urls por aplicativo
    path('accounts/', include('accounts.urls')),

    # Chamar o camninho para a view
    path('user/new', UserNew.as_view(), name = 'user-new'),
    path('user/list', UserList.as_view(), name = 'user-list'),
    # Injetar variavel do tipo 'int' para chamar o ID
    path('user/<int:pk>/update', UserUpdate.as_view(), name = 'user-update'),
    path('user/<int:pk>/detail', UserDetail.as_view(), name = 'user-detail'),
    path('user/<int:pk>/delete', UserDelete.as_view(), name = 'user-delete'),
]
