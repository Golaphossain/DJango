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
    my_context={
        "my_text":"this is about me",
        "my_number":123456,
        "my_list":[1234,2345,'absd',4365,312],
        "this is true":True,
    }
    return render(request,"about.html",my_context)

def social_view(*args,**kwargs):
    return HttpResponse("<h1>social</h1>")