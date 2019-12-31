from django import forms
from django.http import HttpResponse,HttpResponseRedirect, Http404
from .models import *
from django.forms.fields import ChoiceField

# Your own form
class ApplicantPilotOutcomeForm(forms.ModelForm):
    class Meta:
        model = ApplicantPilotOutcome
        fields = [
                  "note"
                  ]
