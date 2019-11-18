# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Applicant(models.Model):
    person_uid = models.TextField(blank=True, null=True)
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
    second_major = models.TextField(blank=True, null=True)
    first_minor = models.TextField(blank=True, null=True)
    application_fee_required_ind = models.TextField(blank=True, null=True)
    enrolled_ind = models.TextField(blank=True, null=True)
    finaid_applicant_ind = models.TextField(blank=True, null=True)
    cohort = models.TextField(blank=True, null=True)
    cohort_year = models.TextField(blank=True, null=True)
    award_appl_count = models.FloatField(blank=True, null=True)
    award_offer_count = models.FloatField(blank=True, null=True)
    award_total_amount = models.FloatField(blank=True, null=True)
    award_inst_amount = models.FloatField(blank=True, null=True)
    award_gov_amount = models.FloatField(blank=True, null=True)
    family_total_indebtedness_amount = models.FloatField(blank=True, null=True)
    fdl_sub_unsub_loan_amount = models.FloatField(blank=True, null=True)
    parent_priv_loan_amount = models.FloatField(blank=True, null=True)
    sport_activity = models.TextField(blank=True, null=True)
    sport_ind = models.FloatField(blank=True, null=True)
    fm_tfc = models.FloatField(blank=True, null=True)
    fm_gross_need = models.FloatField(blank=True, null=True)
    fm_unmet_need = models.FloatField(blank=True, null=True)
    total_offer_amount = models.FloatField(blank=True, null=True)
    resource_amount = models.FloatField(blank=True, null=True)
    pell_efc = models.FloatField(blank=True, null=True)
    family_in_college = models.FloatField(blank=True, null=True)
    family_size = models.FloatField(blank=True, null=True)
    marital_status_ind = models.TextField(blank=True, null=True)
    housing = models.FloatField(blank=True, null=True)
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
    days_to_deadline = models.FloatField(blank=True, null=True)
    days_to_enrollment = models.FloatField(blank=True, null=True)
    latest_secondary_school_desc = models.TextField(blank=True, null=True)
    secondary_school_percentile = models.FloatField(blank=True, null=True)
    secondary_school_size = models.FloatField(blank=True, null=True)
    secondary_school_reported_gpa = models.FloatField(blank=True, null=True)
    secondary_school_distance = models.FloatField(blank=True, null=True)
    secondary_school_urban_centric_locale = models.TextField(blank=True, null=True)
    secondary_school_type = models.TextField(blank=True, null=True)
    visit_count = models.FloatField(blank=True, null=True)
    is_score = models.FloatField(blank=True, null=True)
    test_score_a05 = models.FloatField(blank=True, null=True)
    test_score_s10 = models.FloatField(blank=True, null=True)
    test_score_satt = models.FloatField(blank=True, null=True)
    transfer_out_ind = models.BigIntegerField(blank=True, null=True)
    ftft_enrolled_ind = models.BigIntegerField(blank=True, null=True)
    merit_grant_scale = models.FloatField(blank=True, null=True)
    merit_grant_tier = models.TextField(blank=True, null=True)
    tag = models.BigIntegerField(blank=True, null=True)
    studentno = models.TextField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant'


class ApplicantHistory(models.Model):
    person_uid = models.TextField(blank=True, null=True)
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
    second_major = models.TextField(blank=True, null=True)
    first_minor = models.TextField(blank=True, null=True)
    application_fee_required_ind = models.TextField(blank=True, null=True)
    enrolled_ind = models.TextField(blank=True, null=True)
    finaid_applicant_ind = models.TextField(blank=True, null=True)
    cohort = models.TextField(blank=True, null=True)
    cohort_year = models.TextField(blank=True, null=True)
    award_appl_count = models.FloatField(blank=True, null=True)
    award_offer_count = models.FloatField(blank=True, null=True)
    award_total_amount = models.FloatField(blank=True, null=True)
    award_inst_amount = models.FloatField(blank=True, null=True)
    award_gov_amount = models.FloatField(blank=True, null=True)
    family_total_indebtedness_amount = models.FloatField(blank=True, null=True)
    fdl_sub_unsub_loan_amount = models.FloatField(blank=True, null=True)
    parent_priv_loan_amount = models.FloatField(blank=True, null=True)
    sport_activity = models.TextField(blank=True, null=True)
    sport_ind = models.FloatField(blank=True, null=True)
    fm_tfc = models.FloatField(blank=True, null=True)
    fm_gross_need = models.FloatField(blank=True, null=True)
    fm_unmet_need = models.FloatField(blank=True, null=True)
    total_offer_amount = models.FloatField(blank=True, null=True)
    resource_amount = models.FloatField(blank=True, null=True)
    pell_efc = models.FloatField(blank=True, null=True)
    family_in_college = models.FloatField(blank=True, null=True)
    family_size = models.FloatField(blank=True, null=True)
    marital_status_ind = models.TextField(blank=True, null=True)
    housing = models.FloatField(blank=True, null=True)
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
    days_to_deadline = models.FloatField(blank=True, null=True)
    days_to_enrollment = models.FloatField(blank=True, null=True)
    latest_secondary_school_desc = models.TextField(blank=True, null=True)
    secondary_school_percentile = models.FloatField(blank=True, null=True)
    secondary_school_size = models.FloatField(blank=True, null=True)
    secondary_school_reported_gpa = models.FloatField(blank=True, null=True)
    secondary_school_distance = models.FloatField(blank=True, null=True)
    secondary_school_urban_centric_locale = models.TextField(blank=True, null=True)
    secondary_school_type = models.TextField(blank=True, null=True)
    visit_count = models.FloatField(blank=True, null=True)
    is_score = models.FloatField(blank=True, null=True)
    test_score_a05 = models.FloatField(blank=True, null=True)
    test_score_s10 = models.FloatField(blank=True, null=True)
    test_score_satt = models.FloatField(blank=True, null=True)
    transfer_out_ind = models.BigIntegerField(blank=True, null=True)
    ftft_enrolled_ind = models.BigIntegerField(blank=True, null=True)
    merit_grant_scale = models.FloatField(blank=True, null=True)
    merit_grant_tier = models.TextField(blank=True, null=True)
    tag = models.BigIntegerField(blank=True, null=True)
    studentno = models.TextField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_history'


class ApplicantPilot(models.Model):
    person_uid = models.TextField(blank=True, null=True)
    net_revenue = models.FloatField(blank=True, null=True)
    optimal_step = models.FloatField(blank=True, null=True)
    discount_rate = models.FloatField(blank=True, null=True)
    likelihood_after = models.FloatField(blank=True, null=True)
    likelihood_before = models.FloatField(blank=True, null=True)
    unmet_need_after = models.FloatField(blank=True, null=True)
    unmet_need_before = models.FloatField(blank=True, null=True)
    additional_grant = models.FloatField(blank=True, null=True)
    target_ind = models.BigIntegerField(blank=True, null=True)
    pilot_ind = models.BigIntegerField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_pilot'


class ApplicantPilotOutcome(models.Model):
    id = models.TextField(blank=True, null=True)
    applicant_pilot_id = models.TextField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_pilot_outcome'


class ApplicantPrediction(models.Model):
    person_uid = models.TextField(db_column='PERSON_UID', blank=True, null=True)  # Field name made lowercase.
    ftft_enrolled_ind = models.BigIntegerField(db_column='FTFT_ENROLLED_IND', blank=True, null=True)  # Field name made lowercase.
    ftft_enrolled_pred_score = models.FloatField(db_column='FTFT_ENROLLED_PRED_SCORE', blank=True, null=True)  # Field name made lowercase.
    ftft_enrolled_pred_ind = models.BigIntegerField(db_column='FTFT_ENROLLED_PRED_IND', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicant_prediction'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
