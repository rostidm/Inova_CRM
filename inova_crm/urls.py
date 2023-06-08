from django.contrib import admin
from django.urls import path

from inova_app.views import homePage, registerPage, loginPage

urlpatterns = [
    path('login/', loginPage),
    path('register/', registerPage),
    path('admin/', admin.site.urls),
    path('', homePage)
]
