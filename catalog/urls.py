from . import views
from django.conf.urls import url
from django.urls import include, path
from .views import CompanyViewSet, DiscountViewSet

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^discounts/$', views.DiscountListView.as_view(), name='discounts'),
    # url(r'^self/$', views.SelfDiscountListView.as_view(), name='self'),
    url(r'^discount/(?P<pk>\d+)$', views.DiscountDetailView.as_view(), name='discount-detail'),
    path('api/v1/discount/', DiscountViewSet.as_view()),
    path('api/v1/company/', CompanyViewSet.as_view()),

    # url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]
