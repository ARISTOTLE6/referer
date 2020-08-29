
from django import forms 
from uni.models import UNIAFRIKA
class ReportForm(forms.ModelForm):  
    class Meta:  
        model = UNIAFRIKA  
        fields = "__all__" 