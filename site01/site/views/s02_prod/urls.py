from django.urls import path

from site01.site.views.s02_prod import v01_product

urlpatterns = [
    path(r'v01_product', v01_product.View.as_view(), name='製品一覧'),
]
