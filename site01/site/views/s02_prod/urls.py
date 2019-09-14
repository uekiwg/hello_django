from django.urls import path

from site01.site.views.s02_prod import v01_product

urlpatterns = [
    path(r'v01_product/index', v01_product.IndexView.as_view(), name='製品一覧'),
]
