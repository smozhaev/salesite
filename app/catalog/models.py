import datetime
import uuid

from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from simple_history.models import HistoricalRecords


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Sales(models.Model):
    sales = models.CharField(max_length=100)
    # Добавьте другие поля, если необходимо

    def __str__(self):
        return self.sales

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"


class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статус Акции"
        verbose_name_plural = "Статусы Акций"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Хэштег"
        verbose_name_plural = "Хэштеги"


class Discount(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sales = models.ForeignKey(Sales, on_delete=models.SET_NULL, null=True)
    sale_date_start = models.DateField(default=date.today)
    sale_date_end = models.DateField(default=date.today)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=date.today)
    history = HistoricalRecords()

    def clean(self):
        if self.sale_date_start > self.sale_date_end:
            raise ValidationError("Начальная дата не может быть позже конечной даты.")

    clean.short_description = "My Method for dates"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, default=None, blank=True, null=True
    )
    date_time = models.DateTimeField(default=datetime.MINYEAR)
    url = models.URLField(blank=True)
    request_data = models.TextField(blank=True)
    response_code = models.CharField(max_length=3, blank=True)
    os = models.CharField(max_length=20, blank=True)
    http_agent = models.CharField(max_length=20, blank=True)

    def __str__(self):
        if self.user:
            return self.user.username

        return "Anonymous"

    class Meta:
        verbose_name = "Лог пользователя"
        verbose_name_plural = "Логи пользователей"
