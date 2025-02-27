from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Player  # モデルを取得

class PlayerSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Player.objects.all()

    def location(self, obj):
        return f"/hello/player/{obj.slug}/" if hasattr(obj, "slug") else f"/hello/player/{obj.id}/"

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['home', 'news', 'player', 'direct', 'request']

    def location(self, item):
        return reverse(item)

sitemaps = {
    "players": PlayerSitemap,
    "static": StaticViewSitemap,
}
