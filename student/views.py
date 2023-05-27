from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views import View
#user validation
from . import validation
#student model
from .models import Student
#showinf the message to client
from django.contrib import messages
# Create your views here.
from django.views.generic.list import ListView
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
#adding new student logic and give the form to add the new student

class NewStudent(ListView):
    model = Student
    template_name = 'student/newstudent.html'
    context_object_name = 'students'
    ordering = ['id']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context data here if needed
        return context
        #return render(request,'student/newStudent.html',{'student':student})
    
    #handling the student data coming for the server side post request
class validateStudent(View):  
    def post(self,request):
        #getting the form data
        name=request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        marks = request.POST.get('marks')
        sid= request.POST.get('id')
        
        #once we get the dat from client side we wil validate at server side...
        isCorrect = validation.validateStudentInfo(name,age,gender,marks,sid)
        #if there is no error with student details, saving the data in the database 
        if isCorrect['status']:
            
            #cgecking new student id already exist or not
            isexist = Student.objects.filter(studentid = sid).exists()
            
            if isexist:
                messages.error(request,"Student Id Already Exist")
            else:
                
                Student.objects.create(studentName=name, age=age, gender=gender, marks=marks, studentid=sid).save()
                messages.success(request,"Student Added Successfully")
            
        else:
            messages.error(request,isCorrect['message'])
        #redirecting to the same page
        return HttpResponseRedirect('/student/service/')
    



#deleting the student by id

class DeleteStudent(View):
    def get(self, request,id):
        #checking the id exist or not 
        isexist = Student.objects.filter(studentid = id)
        
        if isexist.exists():
            #deleting the student
            Student.objects.get(studentid = id).delete()
            messages.success(request,f"Student having id {id} is deleted successfully")
            return HttpResponseRedirect('/student/service/')
        else:
            return HttpResponse(f"Student does not exist having id {id}")
            
 
            
#creting the api link 
class StundeDetails(ListView):
    model = Student
    template_name = 'student/studentinfo.html'
    context_object_name = 'students'
    ordering = ['id']
    #five record per page
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context data here if needed
        return context
    
    
#filtring the result
class FilterStudentOptions(ListView):
    model = Student
    template_name = 'student/studentinfo.html'
    context_object_name = 'students'
    ordering = ['id']
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        # Get the filter value from the request parameters
        filter_value = self.request.GET.get('mark')
        filter_option = self.request.GET.get('marks')
        
        # Apply the filter if the value is provided
        if filter_value:
            if filter_option == 'l':
                queryset = queryset.filter(marks__lte = filter_value )
            else :
                queryset = queryset.filter(marks__gt =filter_value)
                
                
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here if needed
        return context