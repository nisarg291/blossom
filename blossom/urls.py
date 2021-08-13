"""blossom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('BlossomEducation',views.BlossomEducation,name="BlossomEducation"),
    path('BlossomImmigration',views.BlossomImmigration,name="BlossomImmigration"),
    path("BlossomCoaching",views.BlossomCoaching,name="BlossomCoaching"),
    path('Spoken/',views.Spoken,name="Spoken"),
    path('Ielts/',views.Ielts,name="Ielts"),
    path("Personality/",views.Personality,name="Personality"),
    path('courses',views.Courses,name="Courses"),
    path('aboutus',views.AboutUs,name="AboutUs"),
    path("UpCommingEvents",views.UpCommingEvents,name="UpCommingEvents"),
    path("Contact",views.Contact,name="Contact"),
    path("Gallary",views.Gallary,name="Gallary"),
    path('USA',views.USA,name="USA"),
    path('Australia',views.Australia,name="Australia"),
    path("Canada",views.Canada,name="Canada"),
    path("NewZealand",views.NewZealand,name="NewZealand"),
    path("Poland",views.Poland,name="Poland"),
    path("Germany",views.Germany,name="Germany"),
    path("UK",views.UK,name="UK"),
    
    
    

]
