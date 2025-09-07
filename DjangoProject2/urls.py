from django.contrib import admin
from django.urls import path, include

from allauth.account.decorators import secure_admin_login
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # ADD THIS LINE
    path('university_detail/<int:pk>/', views.university_detail, name='university_detail'),

    # path('', views.home, name='home'),
    path('', include('core.urls')),
    # Your home page, if you have one
path('api/', include('core.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/login/', secure_admin_login(admin.site.login), name='admin_login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

# DjangoProject2/DjangoProject2/urls.py

