from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _


class Goods(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=200, blank=True, )
    quantity = models.FloatField(verbose_name=_('Quantity'), validators=[MinValueValidator(Decimal('0.01'))]
                                 )
    price = models.DecimalField(verbose_name=_('Price'),
                                decimal_places=2, max_digits=12,
                                validators=[MinValueValidator(Decimal('0.00'))]
                                )

    def get_absolute_url(self):
        return "/"

    @property
    def total_price(self):
        return self.quantity * float(self.price)

    def __str__(self):
        return self.name, self.quantity, self.price, self.total_price


