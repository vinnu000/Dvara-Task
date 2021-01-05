from django.db import models


class Category(models.Model):
    categories = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.categories
    
    class Meta:
        db_table = 'category'


class SubCategory(models.Model):
    subcategory = models.CharField(max_length=30, null=True, blank=True)
    category    = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True, blank=True)
        
    class Meta:
        db_table = 'subcategory'
