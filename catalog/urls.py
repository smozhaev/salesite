from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^discounts/$', views.DiscountListView.as_view(), name='discounts'),
    # url(r'^self/$', views.SelfDiscountListView.as_view(), name='self'),
    url(r'^discount/(?P<pk>\d+)$', views.DiscountDetailView.as_view(), name='discount-detail'),
    # url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]
