from django import forms
from .models import Employee, Course, Department, Project


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"




class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


