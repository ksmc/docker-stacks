from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import default
# Create your models here.

###################### DB TABLES ################################
class Health(models.Model):
    fips = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    county_name = models.TextField(blank=True, null=True)
    premature_death = models.IntegerField(blank=True, null=True)
    percent_poor_health = models.FloatField(blank=True, null=True)
    percent_smokers = models.FloatField(blank=True, null=True)
    percent_obese = models.FloatField(blank=True, null=True)
    percent_excessive_drinking = models.FloatField(blank=True, null=True)
    number_primary_care_physicians = models.IntegerField(blank=True, null=True)
    number_dentists = models.IntegerField(blank=True, null=True)
    number_mental_health_providers = models.IntegerField(blank=True, null=True)
    nerumb_diabetics = models.IntegerField(blank=True, null=True)
    number_single_parent_households = models.IntegerField(blank=True, null=True)
    number_social_organizations = models.IntegerField(blank=True, null=True)
    number_violent_crimes = models.IntegerField(blank=True, null=True)
    percent_mental_distress = models.FloatField(blank=True, null=True)
    range_drug_overdose_mortality_rate = models.TextField(blank=True, null=True)
    costs = models.FloatField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    percent_65_over = models.FloatField(blank=True, null=True)
    state_abbr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health'

class TreatmentCenter(models.Model):
    otpid = models.IntegerField(blank=True, null=True)
    program_name = models.TextField(blank=True, null=True)
    dba = models.TextField(blank=True, null=True)
    program_address = models.TextField(blank=True, null=True)
    program_city = models.TextField(blank=True, null=True)
    zipcode = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    program_state_abbr = models.TextField(blank=True, null=True)
    program_county = models.TextField(blank=True, null=True)
    fips = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'treatment_center_full'

class LimsDrugTest(models.Model):
    
#     countynm = models.TextField(blank=True, null=True)
    stabbr = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    fips = models.TextField(blank=True, null=True)
    
    pop_total = models.IntegerField(blank=True, null=True)
    m_total = models.IntegerField(blank=True, null=True)
    f_total = models.IntegerField(blank=True, null=True)
    m_15_24 = models.IntegerField(blank=True, null=True)
    f_15_24 = models.IntegerField(blank=True, null=True)
    median_income = models.IntegerField(blank=True, null=True)
    vacancy = models.IntegerField(blank=True, null=True)
    rent_occupied = models.IntegerField(blank=True, null=True)
    median_rent = models.IntegerField(blank=True, null=True)
    
    kpi_1 = models.IntegerField(blank=True, null=True)
    kpi_2 = models.IntegerField(blank=True, null=True)
    kpi_3 = models.IntegerField(blank=True, null=True)
    kpi_4 = models.IntegerField(blank=True, null=True)
    kpi_5 = models.IntegerField(blank=True, null=True)
    kpi_6 = models.IntegerField(blank=True, null=True)
    
    kpi_1_scd = models.IntegerField(blank=True, null=True)
    kpi_1_cancer = models.IntegerField(blank=True, null=True)
    kpi_1_hospice = models.IntegerField(blank=True, null=True)
    kpi_1_other = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'lims_drug_test'

class NationwideReport(models.Model):
    year=models.IntegerField(blank=True, null=True)
    quarter=models.TextField(blank=True, null=True)
    fy_code=models.TextField(blank=True, null=True)
    kpi_1=models.IntegerField(blank=True, null=True)
    kpi_2=models.IntegerField(blank=True, null=True)
    kpi_3=models.IntegerField(blank=True, null=True)
    kpi_4=models.IntegerField(blank=True, null=True)
    kpi_1_new=models.IntegerField(blank=True, null=True)
    kpi_2_new=models.IntegerField(blank=True, null=True)
    kpi_3_new=models.IntegerField(blank=True, null=True)
    kpi_4_new=models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'nationwide_report'

class Counties(models.Model):
    county_id = models.TextField(blank=True, null=True)
    county_name = models.TextField(blank=True, null=True)
    state_abbr = models.TextField(blank=True, null=True)
    state_fp = models.TextField(blank=True, null=True)
    county_fp = models.TextField(blank=True, null=True)
    class_fp = models.TextField(blank=True, null=True)
    county_short = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'counties'

class Drug(models.Model):
    drug_id = models.TextField(primary_key=True)
    propreitary_name = models.TextField()
    nonpropreitary_name = models.TextField(blank=True, null=True)
    strength = models.TextField(blank=True, null=True)
    active_ingred_unit = models.TextField(blank=True, null=True)
    product_type_name = models.TextField(blank=True, null=True)
    dosage_from_name = models.TextField(blank=True, null=True)
    route_name = models.TextField(blank=True, null=True)
    start_marketing_date = models.DateField(blank=True, null=True)
    end_marketing_date = models.DateField(blank=True, null=True)
    application_num = models.TextField(blank=True, null=True)
    marketing_cate = models.TextField(blank=True, null=True)
    labeler_name = models.TextField(blank=True, null=True)
    substance_name = models.TextField(blank=True, null=True)
    pharm_classes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s'  % (self.drug_id, self.propreitary_name)
    
    def __str__(self):
        return self.drug_id
    
    def get_absolute_url(self):
        return reverse('loss_manager:drug_update', kwargs={'id':self.drug_id})

    class Meta:
        managed = False
        db_table = 'DRUG'

class LossType(models.Model):
    loss_type_id = models.TextField(primary_key=True)
    
    def __unicode__(self):
        return self.loss_type_id
    
    def __str__(self):
        return self.loss_type_id

    class Meta:
        managed = False
        db_table = 'LOSS_TYPE'


class OutcomeType(models.Model):
    outcome_id = models.TextField(primary_key=True)
    
    def __unicode__(self):
        return self.outcome_id
    
    def __str__(self):
        return self.outcome_id
    
    class Meta:
        managed = False
        db_table = 'OUTCOME_TYPE'


class Facilities(models.Model):
    facility_id = models.TextField(primary_key=True)
    facility_name = models.TextField(blank=True, null=True)
    address = models.TextField()
    city = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)
    county = models.TextField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    license_id = models.TextField(blank=True, null=True)
    manager_id = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default="Active")
    serial_num = models.IntegerField(blank = True, null=True)
    
    def __unicode__(self):
        return self.facility_id
    
    def __str__(self):
        return self.facility_id
    
    def get_absolute_url(self):
        return reverse('loss_manager:facility_detail', kwargs={'id':self.serial_num})

    class Meta:
        managed = False
        db_table = 'FACILITIES'


class LossDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    loss = models.ForeignKey('LossRecord', on_delete=models.CASCADE, related_name="loss_des")
#     drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    drug_id = models.TextField()
    strength = models.TextField(blank=True, null=True)
    uom = models.TextField(blank=True, null=True)  # Field name made lowercase.
    form = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    fuzzy_name = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.fuzzy_name
    
    def __str__(self):
        return self.fuzzy_name
    
    def get_absolute_url(self):
        return reverse('loss_manager:detail_update', kwargs={'id':self.detail_id})

    class Meta:
#         managed = False
        db_table = 'LOSS_DETAIL'


class LossRecord(models.Model):
    loss_id = models.AutoField(primary_key=True)
    loss_date = models.DateField()
    facility = models.ForeignKey(Facilities, on_delete=models.CASCADE)
#     loss_type = models.TextField()
    loss_type = models.ForeignKey(LossType, on_delete=models.SET_DEFAULT, default="Other",related_name="loss_type_des")
#     outcome = models.TextField(blank=True, null=True)
    outcome = models.ForeignKey(OutcomeType, on_delete=models.SET_DEFAULT, default="Investigation Pending", related_name="outcome_des")
    add_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, blank = True, null=True, related_name="user_des")
    value = models.DecimalField(max_digits=65535, decimal_places=2, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.loss_date, 
                                       self.facility, 
                                       self.loss_type.loss_type, 
                                       self.outcome.outcome, 
                                       self.add_time, 
                                       self.update_time,
                                       self.value)
    
    def get_absolute_url(self):
        return reverse('loss_manager:record_detail', kwargs={'id':self.loss_id})
     
    def __str__(self):
        return self.loss_id
    
    class Meta:
        managed = False
        db_table = 'LOSS_RECORD'
        ordering = ('loss_date',)

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)
 
    class Meta:
        managed = False
        db_table = 'auth_group'
 
 
class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
 
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
 
 
class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
 
    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
 
 
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
 
    class Meta:
        managed = False
        db_table = 'auth_user'
 
 
class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
 
    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
 
 
class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
 
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
 
 
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
 
    class Meta:
        managed = False
        db_table = 'django_admin_log'
 
 
class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
 
    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
 
 
class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()
 
    class Meta:
        managed = False
        db_table = 'django_migrations'
 
 
class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
 
    class Meta:
        managed = False
        db_table = 'django_session'

class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'

##################################################################

########################## DB View ###############################
class MphView(models.Model):
    
    detail_id = models.BigIntegerField(primary_key=True)
    loss_date = models.DateField()
    facility = models.TextField()
    loss_type = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=65535, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    drug_name = models.TextField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)
    county = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    lon = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = "MPH_VIEW"