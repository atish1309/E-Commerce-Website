from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()

class AddToShopListForm(forms.Form):
    quantity = forms.IntegerField()