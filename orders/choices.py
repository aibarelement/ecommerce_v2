from django.db import models


class OrderStatusChoices(models.TextChoices):
    New = 'New'
    ProcessInProgress = 'ProcessInProgress'
    Paid = 'Paid'
    Cancel = 'Cancel'
