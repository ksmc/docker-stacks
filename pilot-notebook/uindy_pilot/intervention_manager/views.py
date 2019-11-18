import csv

from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.db import connection

# Create your views here.
from intervention_manager.models import *

############# Applicant Pilot ######################## 
def pilot_list(request):
    filter = request.GET.get("filter")
    if filter:
        objects = ApplicantPilotOutcome.objects.filter(
                Q(applicant_pilot__person_uid__icontains=filter) &
                Q(applicant_pilot__target_ind=1) & 
                Q(applicant_pilot__pilot_ind=1)
                ).order_by('-applicant_pilot__likelihood_after','-applicant_pilot__discount_rate')
    else:
        objects = ApplicantPilotOutcome.objects.filter(
                Q(applicant_pilot__target_ind=1) & 
                Q(applicant_pilot__pilot_ind=1)
                ).order_by('-applicant_pilot__likelihood_after','-applicant_pilot__discount_rate')
                
    paginator = Paginator(objects, 25) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
               "objects":queryset,
               "page_request_var": page_request_var,
               }
    return render(request, "pilot/pilot_list.html", context)

def prediction_list(request):
    filter = request.GET.get("filter")
    if filter:
        objects = ApplicantPrediction.objects.filter(
                Q(person_uid__icontains=filter)
                ).order_by('add_time')
    else:
        objects = ApplicantPrediction.objects.all().order_by('add_time')
                
    paginator = Paginator(objects, 25) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
               "objects":queryset,
               "page_request_var": page_request_var,
               }
    return render(request, "prediction/prediction_list.html", context)

def applicant_detail(request,id):
    object = get_object_or_404(Applicant, id=id)
    context = {
               "obj":object
            }
    return render(request, "applicant/applicant_detail.html", context)
