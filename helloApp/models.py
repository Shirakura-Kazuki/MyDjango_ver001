from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)  # 商品名
    price = models.IntegerField()  # 価格
    description = models.TextField()  # 説明

    def __str__(self):
        return self.name
