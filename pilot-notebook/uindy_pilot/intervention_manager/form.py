from django import forms
from django.http import HttpResponse,HttpResponseRedirect, Http404
from urllib import quote_plus #python 2
from .models import *
from django.forms.fields import ChoiceField

# Your own form
class LossRecordForm(forms.ModelForm):
    class Meta:
        model = LossRecord
        fields = [
                  "loss_date",
                  "loss_type",
                  "facility",
                  "value",
                  "outcome",
                  "user"
                  ]
    # # Customize some fields for data validation
    loss_date = forms.DateField(required=True, input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
                              error_messages={'invalid': 'Please follow format mm/dd/yy'})
    value = forms.DecimalField(required=False, max_digits=65535, decimal_places=2, min_value=0,
                               error_messages={'min_value': 'Please enter a non-negative value'})

class LossDetailForm(forms.ModelForm):
    class Meta:
        model = LossDetail
        fields = [
                  "drug_id",
                  "fuzzy_name",
                  "quantity",
                  "strength",
                  "uom",
                  "form",
                  "note"
                  ]
    drug_id = forms.CharField(required=True, widget=forms.TextInput,label='NDC')
    fuzzy_name = forms.CharField(required=False, widget=forms.TextInput,label='Drug Name')
    quantity = forms.IntegerField(required=True, min_value=0,
                                  error_messages={'min_value': 'Please enter a non-negative value'})
    uom = forms.CharField(required=False, widget=forms.TextInput)
    form = forms.CharField(required=False, widget=forms.TextInput)
    strength = forms.CharField(required=False, widget=forms.TextInput)
    
    def clean_drug_id(self):
        id = self.cleaned_data.get('drug_id')
        print id
        try:
            obj = Drug.objects.get(drug_id=id)
            print(obj)
        except:
            raise forms.ValidationError("This NDC numbers does not exist, please update Drug DB!")
        
        return id
    
class FacilitiesForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = [
                  "facility_id",
                  "facility_name",
                  "address",
                  "city",
                  "zip",
                  "county",
                  "lon",
                  "lat",
                  "status"
#                   "license_id",
#                   "manager_id",
                  ]
    STATUS_CHOICES = [
    ("Active", "Active"),
    ("Expired", "Expired"),
    ("Suspended", "Suspended"),
    ("Pending", "Pending"),
    ("Inactive", "Inactive")]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    facility_id = forms.CharField(required=True, widget=forms.TextInput)
    facility_name = forms.CharField(required=True, widget=forms.TextInput)
    city = forms.CharField(required=True, widget=forms.TextInput)
    zip = forms.CharField(required=True, widget=forms.TextInput)
    county = forms.CharField(required=True, widget=forms.TextInput)
    lat = forms.FloatField(required=True, widget=forms.TextInput)
    lon = forms.FloatField(required=True, widget=forms.TextInput)
    address = forms.CharField(required=True, widget=forms.TextInput)

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = [
                    "drug_id",
                    "propreitary_name",
                    "nonpropreitary_name",
                    "strength",
                    "active_ingred_unit",
                    "product_type_name",
                    "dosage_from_name",
                    "route_name",
                    "start_marketing_date",
                    "end_marketing_date",
                    "application_num",
                    "marketing_cate",
                    "labeler_name",
                    "substance_name",
                    "pharm_classes",
                  ]
    drug_id = forms.CharField(required=True, widget=forms.TextInput,label='NDC')
    propreitary_name = forms.CharField(required=True, widget=forms.TextInput)
    nonpropreitary_name = forms.CharField(required=False, widget=forms.TextInput)
    strength = forms.CharField(required=True, widget=forms.TextInput)
    active_ingred_unit = forms.CharField(required=False, widget=forms.TextInput)
    product_type_name = forms.CharField(required=True, widget=forms.TextInput)
    dosage_from_name = forms.CharField(required=True, widget=forms.TextInput)
    route_name = forms.CharField(required=False, widget=forms.TextInput)
    start_marketing_date = forms.DateField(required=False, widget=forms.TextInput)
    end_marketing_date = forms.DateField(required=False, widget=forms.TextInput)
    application_num = forms.CharField(required=False, widget=forms.TextInput)
    marketing_cate = forms.CharField(required=True, widget=forms.TextInput)
    labeler_name = forms.CharField(required=True, widget=forms.TextInput)
    substance_name = forms.CharField(required=False, widget=forms.TextInput)
    