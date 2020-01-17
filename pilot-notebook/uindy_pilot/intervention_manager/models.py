from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import default
# Create your models here.

###################### DB TABLES ################################
class Applicant(models.Model):
    person_uid = models.BigIntegerField(blank=True, null=True)
    academic_year = models.BigIntegerField(blank=True, null=True)
    academic_period = models.TextField(blank=True, null=True)
    aid_year = models.TextField(blank=True, null=True)
    application_number = models.BigIntegerField(blank=True, null=True)
    complete_ind = models.TextField(blank=True, null=True)
    deposit_ind = models.TextField(blank=True, null=True)
    latest_decision = models.TextField(blank=True, null=True)
    inst_admit_any_time_ind = models.TextField(blank=True, null=True)
    student_level = models.TextField(blank=True, null=True)
    appl_accept_any_time_ind = models.TextField(blank=True, null=True)
    inst_accepted_current_ind = models.TextField(blank=True, null=True)
    appl_accept_current_ind = models.TextField(blank=True, null=True)
    inst_denied_ind = models.TextField(blank=True, null=True)
    applicant_withdrawn_ind = models.TextField(blank=True, null=True)
    application_status = models.TextField(blank=True, null=True)
    campus = models.FloatField(blank=True, null=True)
    residency_ind = models.TextField(blank=True, null=True)
    program = models.TextField(blank=True, null=True)
    college = models.TextField(blank=True, null=True)
    degree = models.TextField(blank=True, null=True)
    award_category = models.FloatField(blank=True, null=True)
    major = models.TextField(blank=True, null=True)
    program_classification = models.FloatField(blank=True, null=True)
    application_fee_required_ind = models.TextField(blank=True, null=True)
    enrolled_ind = models.TextField(blank=True, null=True)
    finaid_applicant_ind = models.TextField(blank=True, null=True)
    inactivate_ind = models.BigIntegerField(blank=True, null=True)
    latest_decision_date = models.DateTimeField(blank=True, null=True)
    admissions_population = models.TextField(blank=True, null=True)
    day_to_deadline_application = models.BigIntegerField(blank=True, null=True)
    cohort = models.TextField(blank=True, null=True)
    cohort_year = models.TextField(blank=True, null=True)
    ftft_enrolled_ind = models.BigIntegerField(blank=True, null=True)
    budget_amount_1fee = models.FloatField(blank=True, null=True)
    budget_amount_1tui = models.FloatField(blank=True, null=True)
    budget_amount_2brd = models.FloatField(blank=True, null=True)
    budget_amount_2rom = models.FloatField(blank=True, null=True)
    budget_amount_3bks = models.FloatField(blank=True, null=True)
    budget_amount_4trn = models.FloatField(blank=True, null=True)
    budget_amount_5mis = models.FloatField(blank=True, null=True)
    budget_amount_6pls = models.FloatField(blank=True, null=True)
    award_appl_count = models.FloatField(blank=True, null=True)
    award_offer_count = models.FloatField(blank=True, null=True)
    award_total_amount_org = models.FloatField(blank=True, null=True)
    award_total_amount = models.FloatField(blank=True, null=True)
    award_inst_amount = models.FloatField(blank=True, null=True)
    award_gov_amount = models.FloatField(blank=True, null=True)
    award_filter_out_amount = models.FloatField(blank=True, null=True)
    loan_total_amount = models.FloatField(blank=True, null=True)
    loan_gov_amount = models.FloatField(blank=True, null=True)
    loan_fdl_sub_amount = models.FloatField(blank=True, null=True)
    loan_fdl_unsub_amount = models.FloatField(blank=True, null=True)
    loan_fdl_perkins_amount = models.FloatField(blank=True, null=True)
    loan_other_amount = models.FloatField(blank=True, null=True)
    pell_efc = models.FloatField(blank=True, null=True)
    family_in_college = models.FloatField(blank=True, null=True)
    family_size = models.FloatField(blank=True, null=True)
    marital_status_ind = models.TextField(blank=True, null=True)
    father_highest_grade = models.FloatField(blank=True, null=True)
    mother_highest_grade = models.FloatField(blank=True, null=True)
    support_children_ind = models.TextField(blank=True, null=True)
    income_work = models.FloatField(blank=True, null=True)
    tax_return_filed = models.FloatField(blank=True, null=True)
    fm_parent_total_income = models.FloatField(blank=True, null=True)
    fm_total_income = models.FloatField(blank=True, null=True)
    fm_parent_contribution_income = models.FloatField(blank=True, null=True)
    fm_contribution_income = models.FloatField(blank=True, null=True)
    fm_total_family_contribution = models.FloatField(blank=True, null=True)
    priority_uindy_ind = models.FloatField(blank=True, null=True)
    days_to_deadline_fafsa = models.FloatField(blank=True, null=True)
    days_to_enrollment_fafsa = models.FloatField(blank=True, null=True)
    fafsa_filed_ind = models.FloatField(blank=True, null=True)
    fm_parent_contribution_pct = models.FloatField(blank=True, null=True)
    coa = models.FloatField(blank=True, null=True)
    gross_need = models.FloatField(blank=True, null=True)
    aid_gift = models.FloatField(blank=True, null=True)
    aid_total = models.FloatField(blank=True, null=True)
    unmet_need = models.FloatField(blank=True, null=True)
    latest_secondary_school_desc = models.TextField(blank=True, null=True)
    latest_secondary_school_name = models.TextField(blank=True, null=True)
    secondary_school_percentile = models.FloatField(blank=True, null=True)
    secondary_school_size = models.FloatField(blank=True, null=True)
    secondary_school_reported_gpa = models.FloatField(blank=True, null=True)
    secondary_school_distance = models.FloatField(blank=True, null=True)
    secondary_school_urban_centric_locale = models.TextField(blank=True, null=True)
    secondary_school_type = models.TextField(blank=True, null=True)
    sport_activity = models.TextField(blank=True, null=True)
    sport_ind = models.FloatField(blank=True, null=True)
    visit_count = models.FloatField(blank=True, null=True)
    is_score = models.FloatField(blank=True, null=True)
    test_score_a05 = models.FloatField(blank=True, null=True)
    test_score_s10 = models.FloatField(blank=True, null=True)
    test_score_satt = models.FloatField(blank=True, null=True)
    aid_package_complete_ind = models.FloatField(blank=True, null=True)
    packaging_group = models.TextField(blank=True, null=True)
    merit_grant_scale = models.FloatField(blank=True, null=True)
    merit_grant_tier = models.TextField(blank=True, null=True)
    tag = models.BigIntegerField(blank=True, null=True)
    studentno = models.TextField(blank=True, null=True)
    seq_id = models.BigIntegerField(blank=True, null=True)
    id = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'applicant'

class ApplicantPilot(models.Model):
    id = models.TextField(primary_key=True)
    person_uid = models.BigIntegerField(blank=True, null=True)
    seq_id = models.BigIntegerField(blank=True, null=True)
    tag = models.BigIntegerField(blank=True, null=True)
    pilot_ind = models.BigIntegerField(blank=True, null=True)
    finaid_applicant_ind = models.BigIntegerField(blank=True, null=True)
    fafsa_filed_ind = models.BigIntegerField(blank=True, null=True)
    aid_package_complete_ind = models.BigIntegerField(blank=True, null=True)
    ftft_enrolled_ind = models.BigIntegerField(blank=True, null=True)
    ftft_enrolled_pred_score = models.FloatField(blank=True, null=True)
    ftft_enrolled_pred_ind = models.BigIntegerField(blank=True, null=True)
    intervention_ind = models.BigIntegerField(blank=True, null=True)
    net_revenue = models.FloatField(blank=True, null=True)
    optimal_step = models.FloatField(blank=True, null=True)
    discount_rate = models.FloatField(blank=True, null=True)
    discount_rate_org = models.FloatField(blank=True, null=True)
    likelihood_after = models.FloatField(blank=True, null=True)
    likelihood_before = models.FloatField(blank=True, null=True)
    additional_grant = models.FloatField(blank=True, null=True)
    target_ind = models.BigIntegerField(blank=True, null=True)
    add_time = models.DateTimeField(default=timezone.now, blank=False, null=False)
    residency_ind = models.BigIntegerField(blank=True, null=True)
    merit_grant_tier = models.BigIntegerField(blank=True, null=True)
    latest_secondary_school_name = models.TextField(blank=True, null=True)
    latest_decision = models.TextField(blank=True, null=True)
    latest_decision_date = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.id
     
    def get_absolute_url(self):
        return reverse('intervention_manager:applicant_detail', kwargs={'id':self.id})
    
    class Meta:
        managed = False
        db_table = 'applicant_pilot'


class ApplicantPilotOutcome(models.Model):
    id = models.TextField(primary_key=True)
    update_time_note = models.DateTimeField(default=timezone.now, blank=False, null=False)
    note = models.TextField(blank=True, null=True)
    applicant_pilot = models.ForeignKey(ApplicantPilot)
    applicant = models.ForeignKey(Applicant)
    
    def __str__(self):
        return self.id
    
    def get_applicant_detail(self):
        return reverse('intervention_manager:applicant_detail', kwargs={'id':self.applicant_id})
     
    def get_absolute_url(self):
        return reverse('intervention_manager:pilot_update', kwargs={'id':self.id})
    
    class Meta:
        managed = False
        db_table = 'applicant_pilot_outcome'


########################## DB View ###############################
