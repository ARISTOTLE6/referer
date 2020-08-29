from django.contrib import admin
from .models import UNIAFRIKA

# Register your models here.


class UniAfrikaAdmin(admin.ModelAdmin):
     list_display=('student_name','subject_name','improvement','ability','attitude','date_created','instructor_comment')




admin.site.register(UNIAFRIKA,UniAfrikaAdmin)