from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"contactlist.html")

def about(request):
    return HttpResponse("this is about page")

def contact(request):
    return HttpResponse("this is contact page")

