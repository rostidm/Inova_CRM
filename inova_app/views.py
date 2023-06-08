from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'inova_app/registerPage.html', context)

def loginPage(request):
    context = {}
    return render(request, 'inova_app/loginPage.html')


def homePage(request):
    return render(request, "inova_app/homePage.html")

