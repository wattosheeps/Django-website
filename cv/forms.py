from django import forms

from .models import Summary
from .models import Qualification
from .models import Experience
from .models import Skill
class SummaryForm(forms.ModelForm):
    
    class Meta:
        model = Summary
        fields = ('text',)
class DateInput(forms.DateInput):
    input_type = 'date'
class QualificationForm(forms.ModelForm):
    
    class Meta:
        model = Qualification
        fields = ('date_start','date_end','location','description',)
        widgets = {
            'date_start': DateInput(),
            'date_end': DateInput(),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('date_start','date_end','location','duties','description',)
        labels = {
            'date_start': 'Start Date',
            'date_end': 'End Date',
            'location': 'Buisness/Company',
            'description': 'Description',
            'duties': 'Duties while working'
        }
        widgets = {
            'date_start': DateInput(),
            'date_end': DateInput(),
        }
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('heading','info',)