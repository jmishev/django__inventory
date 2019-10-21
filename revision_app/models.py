from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Sum


class Goods(models.Model):
    name = models.CharField(default='  ', max_length=200, blank=True)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)


    def get_absolute_url(self):
        return "http://127.0.0.1:8000/"


    @property
    def total_price(self):
        return self.quantity*self.price

    def __str__(self):
        return self.name, self.quantity, self.price, self.total_price

    def calc_total(self):
        return Goods.objects.aggregate(Sum('total_price'))


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

