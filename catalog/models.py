import uuid

from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Sales(models.Model):
    sales = models.CharField(max_length=100)
    # Добавьте другие поля, если необходимо

    def __str__(self):
        return self.sales

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус Акции'
        verbose_name_plural = 'Статусы Акций'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'


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


    def clean(self):
        if self.sale_date_start > self.sale_date_end:
            raise ValidationError("Начальная дата не может быть позже конечной даты.")

    clean.short_description = 'My Method for dates'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


# class DiscountInstance(models.Model):
#     """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4,
#                           help_text="Unique ID for this particular book across whole library")
#     discount = models.ForeignKey('Discount', on_delete=models.RESTRICT, null=True)
#     due_back = models.DateField(null=True, blank=True)
#     borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#
#     @property
#     def is_overdue(self):
#         """Determines if the book is overdue based on due date and current date."""
#         return bool(self.due_back and date.today() > self.due_back)
#
#     LOAN_STATUS = (
#         ('d', 'Maintenance'),
#         ('o', 'On loan'),
#         ('a', 'Available'),
#         ('r', 'Reserved'),
#     )
#
#     status = models.CharField(
#         max_length=1,
#         choices=LOAN_STATUS,
#         blank=True,
#         default='d',
#         help_text='Book availability')
#
#     class Meta:
#         ordering = ['due_back']
#         permissions = (("can_mark_returned", "Set book as returned"),)
#
#     def __str__(self):
#         """String for representing the Model object."""
#         return '{0} ({1})'.format(self.id, self.discount.title)
#


