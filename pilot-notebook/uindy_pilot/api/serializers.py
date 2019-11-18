from urllib import quote_plus #python 2
############
from rest_framework.serializers import (
                                        ModelSerializer,
                                        HyperlinkedRelatedField,
                                        HyperlinkedIdentityField, 
                                        SlugRelatedField,
                                        Serializer
                                        )
############
from rest_framework import serializers
from api.models import *
from django.contrib.admin.utils import lookup_field
############# TreatmentCenters ################
class TreatmentCentersListSerializer(ModelSerializer):
    
    class Meta:
        model = TreatmentCenter
        fields = ('otpid','fips','latitude','longitud')
# 

class TreatmentCentersDetailSerializer(ModelSerializer):
    
    class Meta:
        model = TreatmentCenter
        fields = ('otpid','program_name', 'program_name','dba','program_address','program_city','zipcode','telephone','program_state_abbr','program_county','fips')

############## Health #########################
class HealthDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Health

############## LimsDrugTest ###################
class LimsDrugTestListSerializer(ModelSerializer):
    
    class Meta:
        model = LimsDrugTest

class NationwideReportListSerializer(ModelSerializer):
    
    class Meta:
        model = NationwideReport

############## Facility #######################
class FacilityListSerializer(ModelSerializer):
    
    class Meta:
        model = Facilities
        fields = ('facility_name','address', 'city',  'zip', 'county', 'lon', 'lat')

############## Record #######################
class RecordListSerializer(ModelSerializer):
    
    class Meta:
        model = LossRecord
        fields = ('loss_id', 'loss_date', 'facility', 'value','loss_type','outcome','add_time','update_time')

############## Detail #######################
class DetailListSerializer(ModelSerializer):
    
    class Meta:
        model = LossDetail
        fields = ('detail_id','loss', 'fuzzy_name', 'quantity', 'strength', 'form','uom')
