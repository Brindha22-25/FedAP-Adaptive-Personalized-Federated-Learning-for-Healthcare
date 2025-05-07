"""
URL configuration for altruist project.
from patients import views
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from patients.views import profile_page
import doctors.views
from django.conf.urls.static import static
from django.conf import settings
from patients import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('patients/', include('patients.urls')),
    path('doctors/', include('doctors.urls')),
    #path('admin_tools_stats/', include('admin_tools_stats.urls')),
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views

# from django.conf.urls.static import static
# from django.conf import settings
# # altruist/urls.py

# from patients import views  # Correct import


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
#     path('patients/', include('patients.urls')),
#     path('doctors/', include('doctors.urls')),
#     # path('admin_tools_stats/', include('admin_tools_stats.urls')),  # Only if installed
# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

