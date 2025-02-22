from django.shortcuts import render , redirect ,get_object_or_404
from django.core.paginator import Paginator
from .models import Player

# ニュースページ：ニュースの一覧を表示
def news(request):
    return render(request, 'helloApp/news.html')  # news.htmlを表示

# ホームページ：ホームページを表示
def home(request):
    return render(request, 'helloApp/home.html')  # home.htmlを表示

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