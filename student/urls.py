
from django.urls import path
from . import views as v
from . import views as sv
urlpatterns = [
    
    path('',sv.NewStudent.as_view(),name="newstduent"),
    path('validate/user',sv.validateStudent.as_view(),name="validate"),
    #validating the user then save into the database
    path("delete/student/<str:id>",sv.DeleteStudent.as_view(),name="delete"),
    #api link for the stundets
   
    path("stundetinfo/",sv.StundeDetails.as_view(),name="stundetinfo"),
    
    #applying the filter to the stundet
    path('applyfilter',sv.FilterStudentOptions.as_view(),name="studdent filters")
    
]
