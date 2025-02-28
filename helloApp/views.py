from django.shortcuts import render , redirect ,get_object_or_404
from django.core.paginator import Paginator
import os , json
from .models import Player
from django.conf import settings
from django.views import View
from django.http import HttpResponse


# ニュースページ：ニュースの一覧を表示
def news(request):
    # news.json のパス
    json_path = os.path.join(settings.BASE_DIR, "news.json")

    # JSONファイルを読み込む
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            news_list = json.load(file)
            print( "OKリスト" , news_list)
    except Exception as e:
            print("JSON読み込みエラー:", e)
            news_list = []  # エラー時は空リストにする

    latest_news = news_list[0] if news_list else None  # 最新のお知らせを取得

    return render(request, 'helloApp/news.html' , {"news_list": news_list, "latest_news": latest_news})  # news.htmlを表示

# ホームページ：ホームページを表示
def home(request):
    # news.json のパス
    json_path = os.path.join(settings.BASE_DIR, "news.json")

    # JSONファイルを読み込む
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            news_list = json.load(file)
            latest_news = news_list[0] if news_list else None  # 最新のお知らせを取得
    except Exception as e:
        latest_news = None  # 読み込みエラー時は None
    return render(request, 'helloApp/home.html' , {"latest_news": latest_news})  # home.htmlを表示

# リクエストページ：リクエストページを表示
def request(request):
    return render(request, 'helloApp/request.html')  # request.htmlを表示

def player_detail(request, slug):
    player = get_object_or_404(Player, slug=slug)  # ✅ スラッグでデータ取得
    return render(request, "helloApp/player_detail.html", {"player": player})

# プレイヤーページ：リスト作成バージョン（v2）
def player(request):
    players = Player.objects.all().order_by("id")
    # フィルター処理
    category = request.GET.get("category")
    team = request.GET.get("team")

    if category:
        players = [player for player in players if player.category == category]

    if team:
        players = [player for player in players if player.team == team]

    # ページネーション（1ページ10件）
    paginator = Paginator(players, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'helloApp/player.html', {'page_obj': page_obj, "category": category, "team": team})



# お問い合わせページ：お問い合わせページを表示
def direct(request):
    return render(request, 'helloApp/direct.html')  # direct.htmlを表示

# ✅ プレイヤー詳細（スラッグ経由）
def player_detail(request, slug):
    player = get_object_or_404(Player, slug=slug)  # 🔹 スラッグでデータ取得
    return render(request, "helloApp/player_detail.html", {"player": player})


# ✅ 名前でアクセスしてきた場合にスラッグにリダイレクトするビュー
class PlayerRedirectView(View):
    def get(self, request, name):
        # 🔹 名前から該当するスラッグを取得
        player = get_object_or_404(Player, name=name)
        return redirect('player_detail', slug=player.slug, permanent=True)  # 🔹 301リダイレクト
    
# ポリシー設定ページ：ポリシー設定ページを表示
def policy_1(request):
    return render(request, 'helloApp/policy_1.html')  

# ポリシー設定ページ：ポリシー設定ページを表示
def policy_2(request):
    return render(request, 'helloApp/policy_2.html')  

def question(request):
    return render(request, 'helloApp/question.html')  # question.htmlを表示




def robots_txt(request):
    content = """User-agent: *
Allow: /

Sitemap: https://baseball-love-helper-museum.onrender.com/sitemap.xml"""
    return HttpResponse(content, content_type="text/plain")
