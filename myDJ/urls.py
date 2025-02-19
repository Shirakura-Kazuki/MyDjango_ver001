from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'helloApp/home.html')

urlpatterns = [
    path('', home, name='home'),  # トップページの設定
    path('admin/', admin.site.urls),
    path('hello/', include('helloApp.urls')),
]
