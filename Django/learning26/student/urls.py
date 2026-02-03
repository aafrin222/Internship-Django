from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.studenthome),
    path('list/',views.student_list),
    path('passed/',views.passed_student),
    path('top',views.top_student),
]