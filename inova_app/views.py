from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from inova_app.models import Customer, LoyaltyProgram


def homePage(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers
    }

    return render(request, "inova_app/homePage.html", context)

def programPage(request):
    programs = LoyaltyProgram.objects.all()
    context = {
        "programs": programs
    }

    return render(request, "inova_app/programPage.html", context)


def programDetail(request, pk):
    program = get_object_or_404(LoyaltyProgram, pk=pk)
    context = {
        "program": program
    }

    return render(request, "inova_app/programDetail.html", context)
# !!!!!!!!!!!!!!!!!!!!!
def customerDetail (request, pk):

    customer = Customer.objects.get(id=pk)
    context = {
        "customer": customer
    }

    return render(request, "inova_app/customerDetails.html", context)
