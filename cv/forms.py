from django import forms

from .models import Summary
from .models import Qualification

class SummaryForm(forms.ModelForm):
    
    class Meta:
        model = Summary
        fields = ('text',)
class QualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ('date','location','description',)