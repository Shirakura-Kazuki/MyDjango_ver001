from django.urls import path
from . import views
from .views import player_detail , PlayerRedirectView

urlpatterns = [
    path('news/', views.news, name='news'), # ニュースページ
    path('',views.home , name='home'),  # ホームページ
    path('request/',views.request , name='request'),  # リクエストページ
    path('player/',views.player , name='player'),  # プレイヤーページ
    path('direct/',views.direct , name='direct'),  # お問い合わせページ
    path("player/<slug:slug>/", player_detail, name="player_detail"),  # ✅ スラッグをURLに含める
    path("player/<str:name>/", PlayerRedirectView.as_view(), name="player_redirect"),      
]