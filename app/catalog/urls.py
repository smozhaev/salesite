from . import views
from django.urls import include, path, re_path as url
from rest_framework.routers import DefaultRouter
from .views import DiscountViewSet, DiscountApiView, CompanyViewSet, CompanyApiView
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

# Создаем экземпляр маршрутизатора
router = DefaultRouter()

# Регистрируем ViewSet с маршрутизатором
router.register(r"discount", DiscountViewSet, basename="discount")
router.register(r"company", CompanyViewSet, basename="company")

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^create/$", views.create, name="create"),
    url(r"^discounts/$", views.DiscountListView.as_view(), name="discounts"),
    # url(r'^self/$', views.SelfDiscountListView.as_view(), name='self'),
    url(
        r"^discount/(?P<pk>\d+)$",
        views.DiscountDetailView.as_view(),
        name="discount-detail",
    ),
    path("api/v1/", include(router.urls)),
    path("api/v1/discountApi/", DiscountApiView.as_view(), name="discountApi"),
    path("api/v1/companyApi/", CompanyApiView.as_view(), name="companyApi"),
    # url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
