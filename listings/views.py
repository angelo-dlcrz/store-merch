from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>These are our merch!</p>')

def contact(request):
    return HttpResponse("<h1>Contact Us</h1> <p>We'd love to hear from you!</p>")
