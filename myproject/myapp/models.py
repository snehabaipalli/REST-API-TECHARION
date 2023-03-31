from django.db import models
from django.forms import ValidationError

# Create your models here.
class student(models.Model):
    student_id=models.CharField(max_length=50,default=0)
    name=models.CharField(max_length=200)
    dob=models.DateTimeField()
    gender=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media', default='profile_pig.png')
    marks=models.IntegerField()
    semester=models.CharField(max_length=200, null=True)
    def clean(self):
        ma=student.objects.filter(id=self.student_id,sem=self.semester)
        if self.pk:
            ma=ma.exclude(pk=self.pk)
        if ma.exists():
            raise ValidationError('Marks already Assigned')
##class studentMarks:
    ##student=models.ForeignKey(student)
    ##marks=models.IntegerField()
    ##sem=models.IntegerChoices()