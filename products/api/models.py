from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    

    def  __str__(self):
        return self.name


