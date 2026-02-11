from django.urls import path
from.import views

urlpatterns = [
    path("list/",views.employee_list, name = "employee_list"),
    path("filter/", views.employeeFilter),
    path("create-employee/", views.create_employee, name="create_employee"),
    path("employee-list/", views.employee_list, name="employee_list"),
    path("create-course/", views.create_course, name="create_course"),
    path("course-list/", views.course_list, name="course_list"),
    path("create-department/", views.create_department, name="create_department"),
    path("department-list/", views.department_list, name="department_list"),
    path("create-project/", views.create_project, name="create_project"),
    path("project-list/", views.project_list, name="project_list"),

]


