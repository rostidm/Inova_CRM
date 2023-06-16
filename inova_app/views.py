from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from inova_app.models import Customer


def homePage(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers
    }

    return render(request, "inova_app/homePage.html", context)

def programePage(request):

    return render(request)
# !!!!!!!!!!!!!!!!!!!!!
def customerDetail (request, pk):

    customer = Customer.objects.get(id=pk)
    context = {
        "customer": customer
    }

    return render(request, "inova_app/customerDetails.html", context)
