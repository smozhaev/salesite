from django.contrib import admin
from django.db.models import Q
from .models import Company, Discount, Category,  Sales, Tag,  Status

admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Sales)
admin.site.register(Status)
admin.site.register(Tag)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sales', 'categories', 'sale_date_start', 'sale_date_end', 'status', 'company',)
    list_filter = ('categories', 'sale_date_start', 'sale_date_end', 'status')
    date_hierarchy = 'sale_date_start'
    inlines = []  # атрибут inlines, позволяет добавить встраиваемые объекты (например, редактирование связанных объектов)
    search_fields = ['title']
    raw_id_fields = ['categories']
    def get_queryset(self, request):
        # Получаем фильтр по диапазону дат
        sale_date_start = request.GET.get('sale_date_start')
        sale_date_end = request.GET.get('sale_date_end')
        # Фильтруем объекты модели в соответствии с диапазоном дат
        queryset = super().get_queryset(request)
        if sale_date_start and sale_date_end:
            queryset = queryset.filter(
                Q(start_date__gte=sale_date_start) & Q(end_date__lte=sale_date_end)
            )
        return queryset

    readonly_fields = ('created_at',)

    fieldsets = (
        ('Описание о акции', {
            'fields': ['title', 'description', ('company', 'categories'), 'created_at']
        }),
        ('Информация о акции', {
            'fields': ['sales', ('sale_date_start', 'sale_date_end'), 'status', 'tags']
        }),
    )
    filter_horizontal = ('tags',)






# inlines
# list_display_links









