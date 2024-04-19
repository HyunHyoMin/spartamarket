from django import forms
from .models import Product, Comment

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('title', 'content', 'image')
        labels = {
            'title' : "",
            'content' : "",
            'image' : '상품 이미지'
        }
        
    def save(self, user):
        instance = super().save(commit=False)
        instance.user = user
        instance.save()
        return instance

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ('product', 'user')