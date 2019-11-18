from django.conf.urls import url

from . import views

urlpatterns = [
    ############# Applicant Pilot ######################## 
    url(r'^$', views.pilot_list, name='pilot_list'),
#     url(r'^pilot_update/(?P<id>\d+)$', views.pilot_update, name='pilot_update'),
    
    ############# Applicant Prediction ######################## 
    url(r'^prediction_list/$', views.prediction_list, name='prediction_list'),
    
    ############## Applicant ########################
    url(r'^applicant_detail/(?P<id>\w+)$', views.applicant_detail, name='applicant_detail'),
    
]