from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # どのモデルを使うか指定
        fields = ['name', 'price', 'description']  # 入力フィールドを指定