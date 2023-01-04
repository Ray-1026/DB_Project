from django.db import models

# Create your models here.
class Course(models.Model):

    college_choices = (
        ('共同課程', '共同課程'),
        ('醫學院', '醫學院'),
        ('牙醫學院', '牙醫學院'),
        ('護理學院', '護理學院'),
        ('藥學院', '藥學院'),
        ('生命科學院', '生命科學院'),
        ('電機學院', '電機學院'),
        ('科技法律學院', '科技法律學院'),
        ('資訊學院', '資訊學院'),
        ('工學院', '工學院'),
        ('理學院', '理學院'),
        ('管理學院', '管理學院'),
        ('生物科技學院', '生物科技學院'),
        ('人社學院', '人社學院'),
        ('客家文化學院', '客家文化學院'),
    )

    courseName = models.CharField(max_length = 50)
    professor = models.CharField(max_length = 30)
    semester = models.CharField(max_length = 20)
    college = models.CharField(max_length = 20, choices = college_choices)
    time = models.CharField(max_length = 10)
    credit = models.DecimalField(max_digits = 2, decimal_places = 0)

    def __str__(self):
        return self.courseName
    
    class Meta:
        db_table = 'Course'
        unique_together = (('courseName', 'professor', 'semester', 'college'),)

class Response(models.Model):

    recommand_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = 'response')
    gradingpolicy = models.TextField(blank = False)
    classMethod = models.TextField(blank = False)
    resp = models.TextField(blank = False)
    recommand = models.CharField(max_length = 1, choices = recommand_choices)

    class Meta:
        db_table = 'Response'