"""
URL configuration for community_events project.

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
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from .views import dashboard, login_page, logut_page
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

app_name = 'events'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('login/', login_page, name='login'),
    path('logout/', logut_page, name='logout'),
    path('accounts/', include('accounts.urls')),
    # path('events/', views.event_list, name='event_list'),
    path('', views.event_list, name='event_list'),
    path('events/', include('events.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('', TemplateView.as_view(template_name="home.html")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
