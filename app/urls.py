from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('/BlossomEducation',views.BlossomEducation,name="BlossomEducation"),
    path('/BlossomImmigration',views.BlossomImmigration,name="BlossomImmigration"),
    path("/BlossomCoaching",views.BlossomCoaching,name="BlossomCoaching")
    

]