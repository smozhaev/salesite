from import_export import resources
from .models import Discount


class DiscountResource(resources.ModelResource):
    class Meta:
        model = Discount
        fields = [
            "id",
            "title",
            "description",
            "company",
            "categories",
            "sales",
            "created_at",
            "sale_date_start",
            "sale_date_end",
            "tags",
        ]

    def dehydrate_title(self, discount):
        # Пример кастомизации поля title
        return discount.title.upper()

    # Добавьте дополнительные методы dehydrate для других полей, если требуется
