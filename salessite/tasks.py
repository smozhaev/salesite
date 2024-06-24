from catalog.services import DatabaseStoreService
from celery import shared_task


@shared_task()
def store_logging():
    service = DatabaseStoreService()
    service.store_cache_in_database()
