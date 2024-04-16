from django.shortcuts import render

def login(request):
    return render(request, "tenassist/login.html",)