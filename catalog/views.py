from django.shortcuts import render, redirect

# Create your views here.
from .models import Discount, Category, Company
from django.views import generic
from .forms import DiscountForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .serializers import CompanySerializer, DiscountSerializer


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
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    # class DiscountDetailView(generic.DiscountDetailView):
    #     model = Discount
    return render(
        request,
        'index.html',
        context={'num_discount': num_discount, 'num_сompany': num_сompany, 'num_сategory': num_сategory,
                 'num_visits': num_visits, },
    )


class DiscountListView(generic.ListView):
    model = Discount


class DiscountDetailView(generic.DetailView):
    model = Discount


def create(request):
    error = ''
    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discounts')
        else:
            error = 'Форма была неверной'

    form = DiscountForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, "catalog/create.html", data)


class DiscountViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer



class CompanyViewSet(generics.ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

