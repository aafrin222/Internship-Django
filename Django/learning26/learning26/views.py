from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")

# def AboutUs(request):
    # return HttpResponse("About")

def AboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")

def movie(request):
    return render(request,"movies.html")

def shows(request):
    return render(request,"shows.html")

def news(request):
    return render(request,"news.html")

def reciepe(request):
    ingredient = ['maggie','maggie masala','cheese','chilli flex','condation milk']
    data = {"name":"maggie","time":15,"ingredient":ingredient}
    return render(request,"reciepe.html",data)

def team(request):
    PlayerList = ['Virat Kohli','Rajat Patidar','Devdutt Padikkal','Swastik Chikara','Jordan Cox','Krunal Pandya','Vihan Malhotra','Jacob Bethell','Swapnil Singh','Mangesh Yadav','Kanishk Chouhan']
    data = {"name": "RCB",
            "Capname": "Rajat Patidar",
            "Trophy": 1,
            "PlayerList": PlayerList}
    return render(request,"team.html",data)