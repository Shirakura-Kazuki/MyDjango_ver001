from django.urls import path
from . import views
from .views import player_detail , PlayerRedirectView
# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import sitemaps
# from .views import robots_txt  # robots.txt のビューを追加



urlpatterns = [
    path('news/', views.news, name='news'), # ニュースページ
    path('',views.home , name='home'),  # ホームページ
    path('request/',views.request , name='request'),  # リクエストページ
    path('player/',views.player , name='player'),  # プレイヤーページ
    path('direct/',views.direct , name='direct'),  # お問い合わせページ
    path("player/<slug:slug>/", player_detail, name="player_detail"),  # ✅ スラッグをURLに含める
    path("player/<str:name>/", PlayerRedirectView.as_view(), name="player_redirect"), 
    path("policy_1/", views.policy_1, name="policy_1"),  # ポリシー設定ページ  
    path("policy_2/", views.policy_2, name="policy_2"),  # ポリシー設定ページ
    path("question/", views.question, name="question"),  # 問い合わせページ
]