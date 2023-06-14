from django.contrib import admin
from django.urls import path

from inova_app.views import homePage, custumerDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage),
    path('<pk>/', custumerDetail)
]
