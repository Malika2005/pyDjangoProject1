from django.shortcuts import render

def junior(req):
    return render(req, "JuniorDjangoDeveloper.html")

def middle(req):
    return render(req, "MiddleDjangoDeveloper.html")

def senior(req):
    return render(req, "SeniorDjangoDeveloper.html")