# myapp/management/commands/export_discounts.py

from django.core.management.base import BaseCommand
from catalog.resources import DiscountResource
from tablib import Dataset

class Command(BaseCommand):
    help = 'Export Discounts to Excel'

    def handle(self, *args, **kwargs):
        dataset = DiscountResource().export()
        with open('discounts.xlsx', 'wb') as f:
            f.write(dataset.export('xlsx'))
        self.stdout.write(self.style.SUCCESS('Successfully exported discounts to discounts.xlsx'))
