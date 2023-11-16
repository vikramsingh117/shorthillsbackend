from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    public_id = models.CharField(max_length=255)  


    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            'product_id': self.id,  
            'title': self.title,
            'description': self.description,
            'public_id': self.public_id,
        }