from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)
    num_purchases = models.IntegerField(default=0)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user.username

    # def make_purchase(self, product_price):
    #     if self.balance >= product_price:
    #         self.balance -= product_price
    #         self.num_purchases += 1
    #         self.save()
    #         return True
    #     else:
    #         return False