from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    CATEGORIES = [
        ('jersey', 'Jersey'),
        ('ball', 'Ball'),
        ('shoes', 'Shoes'),
        ('merch', 'Merchandise'),
        ('gear', 'Gear'),
    ]
    store = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, default="jersey")
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name