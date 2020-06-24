from django import forms

from .models import Summary
from .models import Qualification
from .models import Experience
from .models import Skill
class SummaryForm(forms.ModelForm):
    
    class Meta:
        model = Summary
        fields = ('text',)
class QualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ('date','location','description',)

class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('date','location','duties','description',)

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('heading','info',)