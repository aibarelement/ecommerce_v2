from django.db import models


class UserTypeChoices(models.TextChoices):
    Seller = 'Seller'
    Customer = 'Customer'
