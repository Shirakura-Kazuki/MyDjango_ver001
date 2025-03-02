# from django.contrib.sitemaps import Sitemap
# from django.urls import reverse
# from .models import Player  # モデルを取得

# class PlayerSitemap(Sitemap):
#     changefreq = "daily"
#     priority = 0.8

#     def items(self):
#         return Player.objects.all()

#     def location(self, obj):
#         return f"/hello/player/{obj.slug}/" if hasattr(obj, "slug") else f"/hello/player/{obj.id}/"

# class StaticViewSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.5

#     def items(self):
#         return ['home', 'news', 'player', 'direct', 'request']

#     def location(self, item):
#         return reverse(item)

# sitemaps = {
#     "players": PlayerSitemap,
#     "static": StaticViewSitemap,
# }

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Player  # モデルを取得
from django.utils.timezone import now  # 現在時刻を取得

class PlayerSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Player.objects.all()

    def location(self, obj):
        return f"/hello/player/{obj.slug}/" if hasattr(obj, "slug") else f"/hello/player/{obj.id}/"

    def lastmod(self, obj):
        return obj.updated_at if hasattr(obj, "updated_at") else now()

    def priority(self, obj):
        """重要な選手ページの優先度を上げる"""
        return 1.0 if obj.is_featured else 0.8  # `is_featured` が True の場合は 1.0 にする

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return ['home', 'news', 'player', 'direct', 'request']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        """静的ページの最終更新日（仮にサイト全体の更新日を使用）"""
        return now()

    def priority(self, item):
        """トップページ(home)は 1.0、その他は 0.5"""
        return 1.0 if item == "home" else 0.5

sitemaps = {
    "players": PlayerSitemap(),
    "static": StaticViewSitemap(),
}
