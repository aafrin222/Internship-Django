from django.shortcuts import render 

# 1) Home
def studenthome(request):
    return render(request,"student/studentHome.html")

# Data
student = [
    {'name': 'Aafrin', 'marks': 91},
    {'name': 'Kashish', 'marks': 85},
    {'name': 'Dhvani', 'marks':90},
    {'name': 'Neha', 'marks': 80},
    {'name': 'Akangsha', 'marks':38},
    {'name': 'Priyal', 'marks': 33}
]

# 2) All students (for loop)
def student_list(request):
    return render(request,"student/student_list.html",{"student": student})

# 3) passed students(if condition)
def passed_student(request):
    passed = []
    for s in student:
        if s['marks'] >= 40:
            passed.append(s)
    return render(request,"student/passed_student.html",{"passed":passed})

# Top students(if + for)
def top_student(request):
    toppers = []
    for s in student:
        if s["marks"] >= 80:
            toppers.append(s)
    return render(request,"student/top_students.html",{"toppers":toppers})