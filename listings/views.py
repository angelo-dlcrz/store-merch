from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>My favorite bands are:<p>
        <ul>
            <li>{ bands[0].name }</li>
            <li>{ bands[1].name }</li>
            <li>{ bands[2].name }</li>
            <li>{ bands[3].name }</li>             
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>The available merch listings are:<p>
        <ul>
            <li>{ listings[0].title }</li>
            <li>{ listings[1].title }</li>
            <li>{ listings[2].title }</li>
            <li>{ listings[3].title }</li>             
        </ul>
    """)

def contact(request):
    return HttpResponse("<h1>Contact Us</h1> <p>We'd love to hear from you!</p>")
