from django.db import models
from django.utils.text import slugify
import os

def player_image_path(instance, filename):
    """ プレイヤーごとの画像ファイル名を指定 """
    ext = filename.split('.')[-1]  # 拡張子を取得
    filename = f"{instance.slug}.{ext}"  # 例: ichiro.png
    return os.path.join('images/', filename)

class Player(models.Model):
    category_CHOICES = [
        ('選手', '選手'),
        ('その他', 'その他'),
    ]

    team_CHOICES = [
        ('読売ジャイアンツ', '読売ジャイアンツ'),
        ('阪神タイガース', '阪神タイガース'),
        ('中日ドラゴンズ', '中日ドラゴンズ'),
        ('横浜DeNAベイスターズ', '横浜DeNAベイスターズ'),
        ('広島東洋カープ', '広島東洋カープ'),
        ('東京ヤクルトスワローズ', '東京ヤクルトスワローズ'),
        ('オリックス・バファローズ', 'オリックス・バファローズ'),
        ('福岡ソフトバンクホークス', '福岡ソフトバンクホークス'),
        ('北海道日本ハムファイターズ', '北海道日本ハムファイターズ'),
        ('千葉ロッテマリーンズ', '千葉ロッテマリーンズ'),
        ('埼玉西武ライオンズ', '埼玉西武ライオンズ'),
        ('東北楽天ゴールデンイーグルス', '東北楽天ゴールデンイーグルス'),
        ('大阪近鉄バファローズ', '大阪近鉄バファローズ'),
        ('その他', 'その他'),
    ]

    P_AND_H_CHOICES = [
        ('右投右打', '右投右打'),
        ('右投左打', '右投左打'),
        ('左投左打', '左投左打'),
        ('左投右打', '左投右打'),
        ('右投両打', '右投両打'),
        ('左投両打', '左投両打'),
    ]

    POSITION_CHOICES = [
        ('投手', '投手'),
        ('捕手', '捕手'),
        ('一塁手', '一塁手'),
        ('二塁手', '二塁手'),
        ('三塁手', '三塁手'),
        ('遊撃手', '遊撃手'),
        ('外野手', '外野手'),
        ('指名打者', '指名打者'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # 名前
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)  # スラッグ

    updated_at = models.DateTimeField(auto_now=True)  # 最終更新日を追加
    is_featured = models.BooleanField(default=False)  # 重要な選手かどうか
    
    year = models.IntegerField()  # 年数
    category = models.CharField(max_length=10, choices=category_CHOICES)  # カテゴリ
    team = models.CharField(max_length=100, choices=team_CHOICES)  # チーム
    profile = models.TextField()  # プロフィール

    # 追加フィールド（エラー防止のためデフォルト値を設定）
    date = models.DateField(null=True, blank=True)  # 生年月日（空欄OK）
    place = models.CharField(max_length=100, default="不明")  # 出身地
    school = models.CharField(max_length=100, default="不明")  # 出身校
    p_and_h = models.CharField(max_length=10, choices=P_AND_H_CHOICES, default="その他")  # 投打（選択式）
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default="その他")  # ポジション（選択式）
    total_record = models.TextField(default="記録なし")  # 通算成績
    link = models.URLField(max_length=300, blank=True, null=True)  # 外部リンク
    title = models.TextField(default="受賞タイトルなし")  # タイトル（テキスト）
    award = models.TextField(default="受賞歴なし")  # 表彰（テキスト）
    long_profile = models.TextField(default="プロフィールなし")  # プロフィール（テキスト）
    team_history = models.TextField(default="所属チームなし")  # 所属チーム（テキスト）
    # **プロフィール画像**
    profile_image = models.ImageField(upload_to=player_image_path, blank=True, null=True)  # 画像の保存先
    

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":  # ここで空のスラッグもチェック
            self.slug = slugify(self.name)  #  自動でスラッグを生成
        super().save(*args, **kwargs)
    
    def __str__(self):
        return  f"{self.name} ({self.year})"

class Item(models.Model):
    name = models.CharField(max_length=100)  # 商品名
    price = models.IntegerField()  # 価格
    description = models.TextField()  # 説明

    def __str__(self):
        return self.name
