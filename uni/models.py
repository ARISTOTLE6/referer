from django.db import models
from django.utils import timezone

# Create your models here.

class UNIAFRIKA(models.Model):


    student_name= models.TextField(max_length=30)
    Class=models.TextField(max_length=30,null=True)
    topic_treated=models.TextField(max_length=30,null=True)
    subject_name= models.TextField(max_length=30)
    date_created=models.DateField(timezone.now())
    challenges= models.TextField(max_length=30)
    improvement=models.TextField(max_length=50)
    projection= models.TextField(max_length=30)
    attitude= models.TextField(max_length=30)
    execution= models.TextField(max_length=30)
    ability= models.TextField(max_length=30)
    instructor_name= models.TextField(max_length=30)
    instructor_comment= models.TextField(max_length=30)
    comment_to_instructor= models.TextField(max_length=30)
    comment_to_parent= models.TextField(max_length=30)
  