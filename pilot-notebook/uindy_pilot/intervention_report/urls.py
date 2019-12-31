from django.conf.urls import url

from . import views

urlpatterns = [
    ############# Applicant Pilot ######################## 
    url(r'^$', views.report_list, name='report_list'),
    url(r'^/(?P<year>\d+)$', views.report_detail, name='report_detail'),    
]