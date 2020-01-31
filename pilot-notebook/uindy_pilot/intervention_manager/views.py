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
from intervention_manager.form import *

def _search_parser(filter):
    filter = filter.replace('LIKELIHOOD_AFTER','likelihood_after') \
                    .replace('LIKELIHOOD_BEFORE','likelihood_before') \
                    .replace('ADDITIONAL_GRANT','additional_grant') \
                    .replace('TUITION_DISCOUNT','discount_rate') \
                    .replace('TUITION_NET_REVENUE','net_revenue') \
                    .replace('MERIT_GRANT_TIER','merit_grant_tier') \
                    .replace('LATEST_DECISION','latest_decision') \
                    .replace('HIGH_SCHOOL','latest_secondary_school_name') \
                    .replace('high_school','latest_secondary_school_name') \
                    .replace('PELL_EFC','pell_efc') \
                    .replace('PERSON_UID','person_uid') \
                    .replace('STUDENTNO','studentno') \
                    .replace('SEQ_ID','seq_id') \
                    .replace('PILOT_IND','pilot_ind')
#                     .replace('FINAID_APPLICANT_IND','finaid_applicant_ind') \
#                     .replace('FAFSA_FILED_IND','fafsa_filed_ind') \
#                     .replace('AID_PACKAGE_COMPLETE_IND','aid_package_complete_ind') \
                    
    return [filter]

############# Applicant Pilot ######################## 
def pilot_list(request):
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="admission_pilot_2020.csv"'
        data = ApplicantPilot.objects.filter(
#                     Q(pilot_ind=1) &
                    Q(target_ind=1)
                    ).order_by('-pilot_ind','person_uid')
        writer = csv.writer(response)
        writer.writerow(['studentno','person_uid','seq_id','pilot_ind','residency_ind','merit_grant_tier','pell_efc','latest_secondary_school_name','latest_decision','ftft_enrolled_pred_ind','target_ind','additional_grant','net_revenue','discount_rate','discount_rate_org','likelihood_after','likelihood_before'])
        for row in data:
            rowobj = [row.studentno,row.person_uid,row.seq_id,row.pilot_ind,row.residency_ind,row.merit_grant_tier,row.pell_efc,row.latest_secondary_school_name,row.latest_decision,row.ftft_enrolled_pred_ind,row.target_ind,row.additional_grant,row.net_revenue,row.discount_rate,row.discount_rate_org,row.likelihood_after,row.likelihood_before]
            writer.writerow(rowobj)
        return response 
    else:
        filter = request.GET.get("filter")
        if filter:
            where_clauses = _search_parser(filter)
            objects = ApplicantPilotOutcome.objects.filter(
#                     Q(applicant_pilot__pilot_ind=1) &
                    Q(applicant_pilot__target_ind=1)
                    ).extra(where=where_clauses).order_by('-applicant_pilot__pilot_ind','applicant_pilot__person_uid')
        else:
            objects = ApplicantPilotOutcome.objects.filter(
#                     Q(applicant_pilot__pilot_ind=1) &
                    Q(applicant_pilot__target_ind=1)
                    ).order_by('-applicant_pilot__pilot_ind','applicant_pilot__person_uid')
                    
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


def pilot_update(request, id):
    obj = get_object_or_404(ApplicantPilotOutcome, id=id)
    applicant_pilot = ApplicantPilot.objects.filter(id=id).first()
#     print(applicant_pilot.id)
    applicant = Applicant.objects.filter(id=id).first()
    form = ApplicantPilotOutcomeForm(request.POST or None, instance=obj)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.update_time_note = timezone.now()
        instance.save()
        messages.success(request, "Review Saved", extra_tags='html_safe')
        return redirect("intervention_manager:pilot_list")
    context = {
        "id": obj.id,
        "obj": obj,
        "applicant_pilot":applicant_pilot,
        "applicant":applicant,
        "form":form
    }
    return render(request, "pilot/pilot_form.html", context)


def applicant_detail(request,id):
    object = get_object_or_404(Applicant, id=id)
    context = {
               "obj":object
            }
    return render(request, "applicant/applicant_detail.html", context)

import csv
from django.http import HttpResponse

# def pilot_list_download(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="filename.csv"'
#     data = ApplicantPilot.objects.filter(
#                 Q(pilot_ind=1) &
#                 Q(target_ind=1)
#                 ).order_by('person_uid')
#     writer = csv.writer(response)
#     writer.writerow(['id','person_uid','seq_id','pilot_ind','residency_ind','merit_grant_tier','latest_secondary_school_name','latest_decision','ftft_enrolled_pred_ind','target_ind','additional_grant','net_revenue','discount_rate','discount_rate_org','likelihood_after','likelihood_before'])
#     for row in data:
#         rowobj = [row.id,row.person_uid,row.seq_id,row.pilot_ind,row.residency_ind,row.merit_grant_tier,row.latest_secondary_school_name,row.latest_decision,row.ftft_enrolled_pred_ind,row.target_ind,row.additional_grant,row.net_revenue,row.discount_rate,row.discount_rate_org,row.likelihood_after,row.likelihood_before]
#         writer.writerow(rowobj)
#     return response 