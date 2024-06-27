from . import views
from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DiscountViewSet, DiscountApiView, CompanyViewSet, CompanyApiView
# Создаем экземпляр маршрутизатора
router = DefaultRouter()

# Регистрируем ViewSet с маршрутизатором
router.register(r'discount', DiscountViewSet, basename='discount')
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^discounts/$', views.DiscountListView.as_view(), name='discounts'),
    # url(r'^self/$', views.SelfDiscountListView.as_view(), name='self'),
    url(r'^discount/(?P<pk>\d+)$', views.DiscountDetailView.as_view(), name='discount-detail'),
    path('api/v1/', include(router.urls)),
    path('api/v1/discountApi/', DiscountApiView.as_view(), name='discountApi'),
    path('api/v1/companyApi/', CompanyApiView.as_view(), name='companyApi'),


    # url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]
