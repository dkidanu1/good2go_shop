from django.db import models

from products.models import Product
from django.contrib.auth.models import User


class Comment(models.Model):

    RATE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', default='1')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    body = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
