from django.contrib import admin
from django.urls import path

from inova_app.views import homePage, customerDetail, programPage, programDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage),
    path('<int:pk>/', customerDetail),
    path('programs/', programPage),
    path('programs/<int:pk>/', programDetail, name='loyalty-program-detail'),
]
