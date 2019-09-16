from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

app_name = 'site01'
urlpatterns = [

    #: 多言語対応
    #path('i18n/', include('django.conf.urls.i18n')),

    #: ログイン画面などの共通系
    path(r's01_comn/', include('site01.views.s01_comn.urls')),

    #: 製品情報機能
    path(r's02_prod/', include('site01.views.s02_prod.urls')),

    #: 定義されていないパスの場合、ログイン画面へリダイレクト
    path(r'', RedirectView.as_view(url='/site01/s01_comn/v01_entrance', permanent=False)),
]
