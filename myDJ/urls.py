from django.contrib import admin
from django.urls import path , include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from helloApp.sitemaps import sitemaps
from django.http import HttpResponse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ads_txt(request):
    """ads.txt を提供するビュー"""
    ads_path = os.path.join(BASE_DIR, "static", "ads.txt")  # 正しいパス
    if os.path.exists(ads_path):
        with open(ads_path, "r") as f:
            content = f.read()
        return HttpResponse(content, content_type="text/plain")
    else:
        return HttpResponse("ads.txt not found", status=404)
    
    
def home(request):
    return render(request, 'helloApp/home.html')

urlpatterns = [
    path('', home, name='home'),  # トップページの設定
    path('admin/', admin.site.urls),
    path('hello/', include('helloApp.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),  

    path("ads.txt", ads_txt),  # 追加
]

# 画像ファイルのURLパターンを追加
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    