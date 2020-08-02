from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    print(request.user)
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
    # return HttpResponse("<h1>contact</h1>")
    return render(request,"contact.html",{})

def about_view(request,*args,**kwargs):
    # return HttpResponse("<h1>about world</h1>")
    return render(request,"about.html",{})

def social_view(*args,**kwargs):
    return HttpResponse("<h1>social</h1>")