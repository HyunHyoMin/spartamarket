from django import forms
from accounts.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image', 'content']
        labels = {
            'image' : "프로필 이미지",
            'content' : "자기소개",
        }