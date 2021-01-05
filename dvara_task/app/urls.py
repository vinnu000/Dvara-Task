from django.urls import path
from app.views import CategoryView

urlpatterns = [
    path('', CategoryView.as_view(), name='category_view'),
    path('get-subcategory', CategoryView.get_subcategory, name='get_subcategory'),
]