from urllib import quote_plus #python 2
###########
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth.decorators import login_required
###########
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
                                     ListAPIView, 
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView
                                     )
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.filters import (
                                   SearchFilter,
                                   OrderingFilter,
                                   )

###########
from api.models import *
from api.serializers import * 

############ Health Drug View #############
class LimsHealthList(APIView):
    
    def get(self, request, format=None):
        from django.db import connection
        state = self.request.GET.get('state')
        fips = self.request.GET.get('fips')
        
        with connection.cursor() as cursor:
            if fips:
                cursor.execute('SELECT * FROM lims_drug_test m LEFT JOIN health h ON (m.fips = h.fips) WHERE m.year = %(year)s AND m.fips = %(fips)s', {'year':2014, 'fips':fips})
            else:
                cursor.execute('SELECT * FROM lims_drug_test m LEFT JOIN health h ON (m.fips = h.fips) WHERE m.year = %(year)s AND m.stabbr = %(state)s', {'year':2014, 'state':state})
            result_list = self.dictfetchall(cursor)
        return Response(result_list)
    
    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]    


############ Health #######################
class HealthList(ListAPIView):
    serializer_class = HealthDetailSerializer
    
    def get_queryset(self, *args, **kwards):
        
        state = self.request.GET.get('state')
        fips = self.request.GET.get('fips')
        if fips:
            queryset = Health.objects.filter(
                                             Q(fips=fips)
                                             )
        elif state:
            queryset = Health.objects.filter(
                                             Q(state_abbr=state)
                                             )
        else:
            queryset = Health.objects.all()
        
        return queryset

############ LIMS Test ####################
class LimsRecordsList(ListAPIView):
    serializer_class = LimsDrugTestListSerializer
    
    def get_queryset(self, *args, **kwards):
#         fips = self.request.GET.get('fips')
        state = self.request.GET.get('state')
        fips = self.request.GET.get('fips')
        year = self.request.GET.get('year')
        queryset_list = LimsDrugTest.objects.all()
        if state:
             queryset_list = queryset_list.filter(
                                        Q(stabbr=state))
        if fips:
            queryset_list = queryset_list.filter(
                                        Q(fips=fips)).order_by('year')
        if year:
            queryset_list = queryset_list.filter(
                                            Q(year=year)
                                            )
        return queryset_list

############ Nationwide Report ############
class NationwideReportList(ListAPIView):
    serializer_class = NationwideReportListSerializer
    
    def get_queryset(self, *args, **kwards):
        year = self.request.GET.get('year')
        queryset_list = NationwideReport.objects.all()
        if year:
            queryset_list = queryset_list.filter(
                                        Q(year__gt=int(year))
                                        )
        return queryset_list
            
############ Treatment Center #############
class TreatmentCentersList(ListAPIView):
    serializer_class = TreatmentCentersListSerializer
    
    def get_queryset(self, *args, **kwargs):
#         fips = self.request.GET.get('fips')
        fips = self.request.GET.get('fips')
        state = self.request.GET.get('state')
        zoom = self.request.GET.get('zoom')
        west = self.request.GET.get('west')
        east = self.request.GET.get('east')
        north = self.request.GET.get('north')
        south = self.request.GET.get('south')
        if fips:
            queryset_list = TreatmentCenter.objects.filter(
                                    Q(fips=fips)
                                    ).distinct()
        elif state:
            queryset_list = TreatmentCenter.objects.filter(
                                    Q(program_state_abbr=state)
                                    ).distinct()
        elif zoom: 
            print zoom
            if int(zoom) < 7:
                queryset_list = TreatmentCenter.objects.all()
            elif int(zoom) < 9 and west and east and north and south:
                queryset_list = TreatmentCenter.objects.filter(
                                    Q(latitude__lt=float(north))&
                                    Q(latitude__gt=float(south))&
                                    Q(longitud__gt=float(west))&
                                    Q(longitud__lt=float(east))
                                    ).distinct()
            elif west and east and north and south: 
                queryset_list = TreatmentCenter.objects.filter(
                                    Q(latitude__lt=float(north))&
                                    Q(latitude__gt=float(south))&
                                    Q(longitud__gt=float(west))&
                                    Q(longitud__lt=float(east))
                                    ).distinct()
            else:
                queryset_list = TreatmentCenter.objects.all()
        elif west and east and north and south:
            queryset_list = TreatmentCenter.objects.filter(
                                    Q(latitude__lt=float(north))&
                                    Q(latitude__gt=float(south))&
                                    Q(longitud__gt=float(west))&
                                    Q(longitud__lt=float(east))
                                    ).distinct()
        else:
            queryset_list = TreatmentCenter.objects.all()
        return queryset_list


class TreatmentCentersSearch(ListAPIView):
    serializer_class = TreatmentCentersDetailSerializer
    
    def get_queryset(self, *args, **kwargs):
        fips = self.request.GET.get('fips')
        state = self.request.GET.get('state')
        
        if fips and state:
            queryset_list = TreatmentCenter.objects.filter(
                                    Q(fips=fips)&
                                    Q(program_state_abbr=state)
                                    ).distinct()
        else:
            queryset_list = None
        return queryset_list
    

############ 
class TreatmentCentersDetail(RetrieveAPIView):
    """
    Details of  Treatment Center
    """
    queryset = TreatmentCenter.objects.all()
    serializer_class =  TreatmentCentersDetailSerializer
    lookup_field = 'otpid'

############ Loss Record ##################
class ViewList(APIView):
    """
    List all LossRecord.
    """
    def get(self, request, format=None):
        from django.db import connection
        year = request.GET.get('year')
        if year == None:
            year = 2016
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM "MPH_VIEW" WHERE EXTRACT (YEAR FROM loss_date) = %(year)s', {'year':year})
            result_list = self.dictfetchall(cursor)
        return Response(result_list)
    
    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]    
    
############ Facilities ##################
class FacilityList(ListAPIView):
    """
    List all Facilities.
    """
    serializer_class = FacilityListSerializer
    queryset = Facilities.objects.all()
    
############ Records ##################
class RecordsList(APIView):
    """
    List all Loss Records.
    """
    def get(self, request, format=None):
        from django.db import connection
        year = self.request.GET.get('year')
        if year == None:
            year = 2016
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM "LOSS_RECORD" r LEFT JOIN "FACILITIES" f ON (r.facility_id = f.facility_id) WHERE EXTRACT (YEAR FROM loss_date) = %(year)s ORDER BY loss_date', {'year':year})
            result_list = self.dictfetchall(cursor)
        return Response(result_list)
    
    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]    
    
############ Details ##################
class DetailList(ListAPIView):
    """
    List all Loss Records.
    """
    serializer_class = DetailListSerializer
    queryset = LossDetail.objects.all()

class RecordAgg(APIView):
    """
    list all Loss Records order by time
    """
    def get(self, request, format=None):
        from django.db import connection
        year = self.request.GET.get('year')
        date = self.request.GET.get('date')
        if year == None:
            year = 2016
        if date == None:
            date = '2016-09-01'
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM "LOSS_RECORD" r LEFT JOIN "FACILITIES" f ON (r.facility_id = f.facility_id) WHERE EXTRACT (YEAR FROM loss_date) = %(year)s AND loss_date < %(date)s ORDER BY loss_date', {'year':year, 'date':date})
            result_list = self.dictfetchall(cursor)
        return Response(result_list)
    
    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]    

