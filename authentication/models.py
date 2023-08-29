import logging
import re

from django.contrib.auth.models import User
from django.db import models



logger = logging.getLogger(__name__)


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    saldo = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
