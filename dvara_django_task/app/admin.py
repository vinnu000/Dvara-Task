from django.contrib import admin
from app.models import Category, SubCategory


admin.site.register(Category)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'category')
    ordering = ('id', )
    search_fields = ('subcategory', 'category')
