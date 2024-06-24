from catalog.services import DatabaseStoreService
from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from catalog.models import Discount


@shared_task()
def send_email_task():
    email_address = "amirgataullin04@gmail.com"
    last_discount = Discount.objects.latest('sale_date_start')
    message = f'''{last_discount.title}\n\n{last_discount.description}\n'''\
            f'''Размер скидки: {last_discount.sales}\n{last_discount.company}'''

    users = User.objects.all()
    results = []
    for user in users:
        if user.is_superuser:
            continue
        status = send_mail(
            "Скидки!",
            message,
            None,
            [user.email],
            fail_silently=False,
        )
        results.append(status)
    return f"Всего поль-ей: {len(results)}\nУспешно отправлены: {sum(results)}"

@shared_task
def store_logging():
    service = DatabaseStoreService()
    service.store_cache_in_database()
