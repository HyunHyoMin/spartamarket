from django import forms
from .models import Product, Comment

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ('user',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ('product', 'user')