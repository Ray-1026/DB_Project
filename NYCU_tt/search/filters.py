from django import forms
from .models import *
import django_filters

class CourseFilter(django_filters.FilterSet):
    courseName = django_filters.CharFilter(
        lookup_expr = 'icontains',
        widget = forms.TextInput(attrs={'class':'form-control'})
    )

    professor = django_filters.CharFilter(
        lookup_expr = 'icontains',
        widget = forms.TextInput(attrs={'class':'form-control'})
    )

    college = django_filters.CharFilter(
        widget = forms.Select(choices=(('', '請選擇'),) + Course.college_choices, attrs={'class':'form-control'})
    )

    class Meta:
        model = Course
        fields = '__all__'
