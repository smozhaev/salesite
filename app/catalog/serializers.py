from .models import Discount, Company
from rest_framework import serializers
from django.core.exceptions import ValidationError

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'title', 'description', 'company', 'categories', 'sales', 'created_at', 'sale_date_start', 'sale_date_end', 'tags']

    def validate(self, data):
        if data['sale_date_start'] > data['sale_date_end']:
            raise serializers.ValidationError("Дата начала скидки не может быть позднее даты окончания.")
        return data

    def validate_description(self, value):
        if len(value) > 300:
            raise serializers.ValidationError("Описание слишком длинное. Максимальная длина - 300 символов.")
        return value

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Название скидки не может быть пустым.")
        if len(value) > 100:
            raise serializers.ValidationError("Название слишком длинное. Максимальная длина - 100 символов.")
        return value




class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'description']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Название компании не может быть пустым.")
        if Company.objects.filter(name=value).exists():
            raise serializers.ValidationError("Компания с таким названием уже существует.")
        return value

    def validate_description(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("Описание слишком длинное. Максимальная длина - 500 символов.")
        return value