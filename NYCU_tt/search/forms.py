from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'
        labels = {
            'gradindpolicy':_('評分方式'),
            'classMethod':_('上課方式'),
            'resp':_('心得'),
            'recommand':_('總體推薦度(1~5)'),
        }

class RawCourseForm(forms.Form):
    courseName = forms.CharField()
    professor = forms.CharField()
    semester = forms.CharField()
    time = forms.CharField()
    credit = forms.DecimalField()
    class Meta:
        labels = {
            'gradindpolicy':_('評分方式'),
            'classMethod':_('上課方式'),
            'resp':_('心得'),
            'recommand':_('總體推薦度(1~5)'),
        }

class RawResponseForm(forms.Form):
    gradindpolicy = forms.CharField()
    classMethod = forms.CharField()
    resp = forms.CharField()
    recommand = forms.DecimalField()