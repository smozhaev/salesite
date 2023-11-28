from .models import Discount, Company
from rest_framework import serializers


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['title', 'description', 'company', 'categories', 'sales']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'description']

