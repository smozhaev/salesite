from django.shortcuts import render, redirect

# Create your views here.
from .models import Discount, Category, Company
from django.views import generic
from .forms import DiscountForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .serializers import CompanySerializer, DiscountSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
import datetime

# Импорты Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    # Генерация "количеств" некоторых главных объектов
    num_discount = Discount.objects.all().count()
    num_сompany = Company.objects.all().count()
    num_сategory = Category.objects.all().count()
    # num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    # num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    # class DiscountDetailView(generic.DiscountDetailView):
    #     model = Discount
    return render(
        request,
        "index.html",
        context={
            "num_discount": num_discount,
            "num_сompany": num_сompany,
            "num_сategory": num_сategory,
            "num_visits": num_visits,
        },
    )


class DiscountListView(generic.ListView):
    model = Discount


class DiscountDetailView(generic.DetailView):
    model = Discount


def create(request):
    error = ""
    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("discounts")
        else:
            error = "Форма была неверной"

    form = DiscountForm()

    data = {"form": form, "error": error}

    return render(request, "catalog/create.html", data)


class DiscountApiView(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = [
        "categories",
        "company",
        "tags",
    ]  # Предполагается, что у модели Discount есть поле categories
    search_fields = [
        "title",
        "description",
        "company__name",
    ]  # Добавьте сюда поля, по которым вы хотите осуществлять поиск
    ordering_fields = ["created_at"]

    def get_queryset(self):
        queryset = Discount.objects.all()

        queryset = queryset.filter(
            (
                Q(
                    sale_date_start__range=[
                        datetime.date(2023, 1, 1),
                        datetime.date(2023, 12, 31),
                    ]
                )
                | Q(
                    sale_date_end__range=[
                        datetime.date(2024, 1, 1),
                        datetime.date(2024, 1, 31),
                    ]
                )
            )
            & ~Q(company__name="Старбакс")
        )

        return queryset


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    @action(methods=["GET"], detail=False)
    def statistics(self, request):
        total_discounts = self.queryset.count()
        category_stats = (
            self.queryset.values("categories__name")
            .annotate(count=Count("categories"))
            .order_by("-count")
        )

        statistics_data = {
            "total_discounts": total_discounts,
            "category_stats": category_stats,
        }
        return Response(statistics_data)

    @action(methods=["POST"], detail=True)
    def update_description(self, request, pk=None):
        discount = self.get_object()
        new_description = request.data.get("description", None)

        if new_description is not None:
            discount.description = new_description
            discount.save()
            return Response({"status": "Описание обновлено"}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Новое описание не предоставлено"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class CompanyApiView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        "name"
    ]  # Добавьте сюда поля, по которым вы хотите осуществлять поиск
    ordering_fields = ["description"]

    def get_queryset(self):
        # Регулярные выражения для русских и английских букв
        regex_russian = r"[а-яА-Я]"
        regex_english = r"[a-zA-Z]"

        # Получаем базовый QuerySet
        queryset = Company.objects.all()

        # Применяем фильтрацию
        queryset = queryset.filter(
            (Q(name__iregex=regex_russian) | Q(name__iregex=regex_english))
            & ~Q(name__iexact="Макдональдс")
        )

        return queryset


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
