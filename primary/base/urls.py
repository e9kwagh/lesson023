from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    # path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('career',views.career,name="career"),
    path('curriculum',views.curriculum,name="curriculum"),
    path('trainer',views.trainer,name="trainer"),
    path('student',views.student,name="student"),
     
]


 