"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from . import views
## Deployment
import os
username = os.getenv('USERNAME')
if username:
    urlpatterns = [
        ## For run in AKS
        url(r'^user/{}/pilot/intervention_manager'.format(username), include('intervention_manager.urls', namespace="intervention_manager")),
        url(r'^user/{}/pilot/intervention_report'.format(username), include('intervention_report.urls', namespace="intervention_report")),
        url(r'^user/{}/pilot'.format(username), views.goHome, name = "home"),
    
    ]
else:
    urlpatterns = [
        ## For run in local container
        url(r'^pilot/intervention_manager', include('intervention_manager.urls', namespace="intervention_manager")),
        url(r'^pilot/intervention_report', include('intervention_report.urls', namespace="intervention_report")),
        url(r'^pilot', views.goHome, name = "home"),
        ## For run as localhost
        url(r'^intervention_manager/', include('intervention_manager.urls', namespace="intervention_manager")),
        url(r'^intervention_report/', include('intervention_report.urls', namespace="intervention_report")),
        url(r'^$', views.goHome, name = "home"),
        
    ]

## get static files through external URL
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
