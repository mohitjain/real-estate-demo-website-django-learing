from django.shortcuts import render

# Create your views here.

def index(requet):
    return render(requet, 'listings/listings.html')

def listing(requet):
    return render(requet, 'listings/listing.html')

def search(requet):
    return render(requet, 'listings/search.html')