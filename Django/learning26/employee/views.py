from django.shortcuts import render,redirect
from.models import Employee,Course,Department,Project
from .forms import EmployeeForm, CourseForm,DepartmentForm,ProjectForm
from django.contrib import messages
# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    return render(request,"employee/employee_list.html",{"employees":employees})


def employeeFilter(request):
# Age Filters (gt & gte)
    age_gt = Employee.objects.filter(age__gt=23)
    age_gte = Employee.objects.filter(age__gte=23)

# Salary Ordering (salary & -salary)
    salary_asc = Employee.objects.order_by("salary")
    salary_desc = Employee.objects.order_by("-salary")

# Name Exact Match (exact & iexact)
    name_exact = Employee.objects.filter(name__exact="Ayaan")
    name_iexact = Employee.objects.filter(name__iexact="ayaan")

# Contains (contains & icontains)
    name_contains = Employee.objects.filter(name__contains="a")
    name_icontains = Employee.objects.filter(name__icontains="A")

# StartsWith / EndsWith (Case + Ignore Case)
    name_starts = Employee.objects.filter(name__startswith="A")
    name_istarts = Employee.objects.filter(name__istartswith="a")

    name_ends = Employee.objects.filter(name__endswith="a")
    name_iends = Employee.objects.filter(name__iendswith="A")

# Range
    age_range = Employee.objects.filter(age__range=[20, 30])

# IN Query
    name_in = Employee.objects.filter(name__in=["Ayaan", "Riya"])

# Age Less than / Less than equal
    age_lt = Employee.objects.filter(age__lt=28)    # age < 28
    age_lte = Employee.objects.filter(age__lte=28)  # age <= 28

# Post filter
    developer_emp = Employee.objects.filter(post="Developer")

#Name starts with / ends with
    name_starts_r = Employee.objects.filter(name__startswith="R")
    name_istarts_a = Employee.objects.filter(name__istartswith="a")

    name_ends_a = Employee.objects.filter(name__endswith="a")
    name_iends_n = Employee.objects.filter(name__iendswith="N")

# Multiple condition (AND)
    ayaan_dev = Employee.objects.filter(name="Ayaan", post="Developer")

# IN query (multiple values)
    name_in = Employee.objects.filter(name__in=["Ayaan", "Riya"])

# Salary RANGE
    salary_range = Employee.objects.filter(salary__range=[20000, 50000])






    context = {
        "age_gt": age_gt,
        "age_gte": age_gte,
        "salary_asc": salary_asc,
        "salary_desc": salary_desc,
        "name_exact": name_exact,
        "name_iexact": name_iexact,
        "name_contains": name_contains,
        "name_icontains": name_icontains,
        "name_starts": name_starts,
        "name_istarts": name_istarts,
        "name_ends": name_ends,
        "name_iends": name_iends,
        "age_range": age_range,
        "name_in": name_in,
        "age_lt": age_lt,
        "age_lte": age_lte,
        "developer_emp": developer_emp,
        "name_starts_r": name_starts_r,
        "name_istarts_a": name_istarts_a,
        "name_ends_a": name_ends_a,
        "name_iends_n": name_iends_n,
        "ayaan_dev": ayaan_dev,
        "name_in": name_in,
        "salary_range": salary_range,
    }

    return render(request, "employee/employeeFilter.html", context)







# -------- CREATE EMPLOYEE --------
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Created Successfully!")
            return redirect("create_employee")
    else:
        form = EmployeeForm()

    return render(request, "employee/create_employee.html", {"form": form})


# -------- EMPLOYEE LIST --------
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee/employee_list.html", {"employees": employees})


# -------- CREATE COURSE --------
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course Added Successfully!")
            return redirect("create_course")
    else:
        form = CourseForm()

    return render(request, "employee/create_course.html", {"form": form})

#-----------Course List------------
def course_list(request):
    courses = Course.objects.all()
    return render(request, "employee/course_list.html", {"courses": courses})


def create_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department Added Successfully!")
            return redirect("create_department")
    else:
        form = DepartmentForm()

    return render(request, "employee/create_department.html", {"form": form})


def department_list(request):
    departments = Department.objects.all()
    return render(request, "employee/department_list.html", {"departments": departments})




# -------- CREATE PROJECT --------
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Project Added Successfully!")
            return redirect("create_project")
    else:
        form = ProjectForm()

    return render(request, "employee/create_project.html", {"form": form})


# -------- PROJECT LIST --------
def project_list(request):
    projects = Project.objects.all()
    return render(request, "employee/project_list.html", {"projects": projects})

