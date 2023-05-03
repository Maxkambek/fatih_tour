from django.db import models
from accounts.models import Account
from main.models import TourDate


class Order(models.Model):
    client = models.ForeignKey(Account, on_delete=models.CASCADE)
    tour = models.ForeignKey(TourDate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.phone

