from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class RawCourseForm(forms.Form):
    courseName = forms.CharField(label = '課程名稱')
    professor = forms.CharField(label = '授課教授')
    semester = forms.CharField(label = '修課年度 (ex : 110下)')
    time = forms.CharField(label = '上課時間 (ex : T34)')
    credit = forms.DecimalField(label = '學分數')

class RawResponseForm(forms.Form):
    gradindpolicy = forms.CharField(label = '評分占比')
    classMethod = forms.CharField(label = '上課方式')
    resp = forms.CharField(label = '心得')
    recommand = forms.DecimalField(label = '總體推薦度 (1 ~ 5)')