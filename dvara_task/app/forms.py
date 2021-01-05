from django import forms
from app.models import Category, SubCategory


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = SubCategory
        fields = "__all__"
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
