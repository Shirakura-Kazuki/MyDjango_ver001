from django.contrib import admin
from django.urls import path , include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from helloApp.sitemaps import sitemaps

def home(request):
    return render(request, 'helloApp/home.html')

urlpatterns = [
    path('', home, name='home'),  # トップページの設定
    path('admin/', admin.site.urls),
    path('hello/', include('helloApp.urls')),

    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),  
]

# 画像ファイルのURLパターンを追加
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    