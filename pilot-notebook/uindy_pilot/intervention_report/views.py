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


############# Applicant Pilot ######################## 
def report_list(request):
    context = {
               "years":[{"year":2019},{"year":2020}],
               "current_year": 2020,
               }
    return render(request, "report/report_list.html", context)


def report_detail(request, year):
    context = {
               "year":year,
               }
    return render(request, "report/data_viz/data_viz_{}.html".format(str(year)), context)

