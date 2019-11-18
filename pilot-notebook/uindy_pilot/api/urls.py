from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import *

urlpatterns = [

    ########### Views #################
    url(r'^records/$', ViewList.as_view(), name='view_list'),
#     url(r'^records/(?P<record_id>\d+)/$', views.RecordDetail.as_view(), name='record_detail'),
    
    ########### Tables #################
    url(r'^facilities/$', FacilityList.as_view(), name='facility_api'),
    url(r'^loss_records/$', RecordsList.as_view(), name='record_api'),
    url(r'^loss_details/$', DetailList.as_view(), name='detail_api'),
#     url(r'^facilities/(?P<f_id>\d+)/$', views.FacilityDetail.as_view(), name='facility_detail'),
    url(r'^record_agg/$', RecordAgg.as_view(), name='record_agg'),
    
    url(r'^treatment_centers/$', TreatmentCentersList.as_view(), name='treatment_centers_list_api'),
    url(r'^treatment_centers/(?P<otpid>\d+)$', TreatmentCentersDetail.as_view(), name='treatment_centers_detail_api'),
    url(r'^treatment_centers/search/$', TreatmentCentersSearch.as_view(), name='treatment_centers_search_api'),
    url(r'^lims_records/$', LimsRecordsList.as_view(), name='lims_records_api'),
    url(r'^nationwide_report/$', NationwideReportList.as_view(), name='nationwide_report_api'),
    url(r'^health/$', LimsHealthList.as_view(),name='health_api')
]