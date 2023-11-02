from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "tracker/index.html", {})
def addGrocer(request):
    return render(request, "tracker/addGrocer.html", {})
def editGrocer(request):
    pass
def grocerList(request):
    pass
def groceryPurchase(request):
    pass
def compareGrocers(request):
    pass
