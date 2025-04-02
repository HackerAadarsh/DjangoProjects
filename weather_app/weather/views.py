from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse(' Welcome to the Weather App!')