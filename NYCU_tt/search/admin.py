from django.contrib import admin
from .models import *

# Register your models here.
class Course_Admin(admin.ModelAdmin):
    list_display = ('id', 'courseName', 'professor', 'semester', 'college', 'time', 'credit')

class Response_Admin(admin.ModelAdmin):
    list_display = ('id', 'course', 'gradingpolicy', 'classMethod', 'resp', 'recommand')

admin.site.register(Course, Course_Admin)
admin.site.register(Response, Response_Admin)