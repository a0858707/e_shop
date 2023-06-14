from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    product_amount= models.IntegerField()
    price = models.FloatField()
    reviews = models.FloatField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return self.name
class UserCart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name