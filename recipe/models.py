from django.db import models

class Taste(models.Model):
    """味"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('味付け', max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    """料理のカテゴリー"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('味付け', max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """レシピ"""
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリー', related_name='recipe')
    taste = models.ForeignKey(Taste, verbose_name='味付け', related_name='recipe')

    def __str__(self):
        return self.taste.name
