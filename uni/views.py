from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import UNIAFRIKA
from .forms import ReportForm
from django.views.generic import ListView,View,DetailView,CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.
# 




def test(request):
    return render(request,'form.html')    


def REPORT_LIST(request):
    report=UNIAFRIKA.objects.all()

   
    return render(request,'report_list.html',{'reports':report})    





def AddForm(request):
    
    
    if request.method=='POST':
        new_student_name = request.POST['student_name']
        new_subject_name = request.POST['subject_name']
        new_Class = request.POST['Class']
        new_topic_treated=request.POST['topic_treated']
        new_improvement =request.POST['improvement']
        new_projection =request.POST['projection']
        
        new_ability =request.POST['ability']
        
        new_date = request.POST['date_created']
        new_execution= request.POST['execution'] 
       
        new_challenges =request.POST['challenges']
        new_attitude =request.POST['attitude']
        new_instructor_name = request.POST['instructor_name']
        new_instructor_comment = request.POST['instructor_comment']
        
        new_comment_to_instructor = request.POST['comment_to_instructor']
        new_comment_to_parent = request.POST['comment_to_parent']
        
        NewUNIAFRIKA = UNIAFRIKA(student_name=new_student_name , subject_name=new_student_name,improvement= new_improvement,ability=new_ability,attitude=new_attitude ,instructor_comment=new_instructor_comment, comment_to_instructor=new_comment_to_instructor,comment_to_parent=new_comment_to_parent, instructor_name=new_instructor_name, execution=new_execution ,challenges=new_challenges ,Class=new_Class,topic_treated=new_topic_treated,projection=new_projection,date_created=new_date)
        
        Is_save=NewUNIAFRIKA.save()
        
        
        
        
        
           
        
        return render(request,'form.html',)

def DELETE_REPORT(request,delete_id):
     report_to_delete =UNIAFRIKA.objects.get(id=delete_id)
     report_to_delete.delete()
     
     return HttpResponseRedirect('/INVENTORY/')

def UPDATE_REPORT(request, update_id):  
    reportUpdate= UNIAFRIKA.objects.get(id=update_id)  
    form = ReportForm(request.POST, instance = reportUpdate)  
    if form.is_valid():  
        form.save()  
        return redirect("/INVENTORY/")  
    return render(request, 'edit.html', {'report_Update': reportUpdate})  


def VIEWS_REPORT_TABLE(request):
    report_table=UNIAFRIKA.objects.all()


    return render(request,'report_table.html',{'report_table':report_table} )


def STUDENT_REPORT(request, student_id):  
    student_report= UNIAFRIKA.objects.get(id=student_id)  
      
     
    return render(request, 'student_report.html', {'student_report': student_report})  


def VIEW(request):
    student_report= UNIAFRIKA.objects.all()
    
   
    return render(request, 'view.html',{'student_report':student_report})

class HomeView(View):
    def get(self,*args,**kwargs):
        context={
            'form':UNIAFRIKA.objects.all()
        }

        return render(self.request,'home.html',context)
   
    

class ABOUT(View):
    def get(self,*args,**kwargs):

        return render(self.request,'about.html')



