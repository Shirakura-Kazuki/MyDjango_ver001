from django.shortcuts import render , redirect ,get_object_or_404
from django.core.paginator import Paginator

from .models import Item
from .forms import ItemForm

# アイテムテーブルの全てを表示（ページ送り・検索）
def item_list(request):
    query = request.GET.get('q', '').strip()  # 検索クエリを取得(デフォルト値：''空文字設定)、.strip()：余分な空白や改行を削除する
    if query:
        Items = Item.objects.filter(name__icontains=query)  # 部分一致検索
    else:
        Items = Item.objects.all()  #全てのデータ取得
    paginator = Paginator(Items, 5)  # 1ページあたり5件表示
    page_number = request.GET.get('page')  # 現在のページ番号を取得
    page_obj = paginator.get_page(page_number)  # 現在のページのデータを取得
    return render(request,'home.html' ,{'page_obj':page_obj , 'query': query} ) 

# 入力フォーム：データベースに追加する入力フォーム
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()  # データベースに保存
            return redirect('item_list')  # データ保存後、一覧ページにリダイレクト
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

# 編集フォーム：データベースのデータの編集・上書き
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # 編集対象のデータを取得
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()  # データを更新
            return redirect('item_list')  # 更新後、一覧ページにリダイレクト
    else:
        form = ItemForm(instance=item)  # 既存データをフォームに表示
    return render(request, 'edit_item.html', {'form': form})

# ニュースページ：ニュースの一覧を表示
def news(request):
    return render(request, 'helloApp/news.html')  # news.htmlを表示

# ホームページ：ホームページを表示
def home(request):
    return render(request, 'helloApp/home.html')  # home.htmlを表示