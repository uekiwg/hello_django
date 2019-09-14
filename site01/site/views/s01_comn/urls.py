from django.urls import path

from site01.site.views.s01_comn import v01_entrance

urlpatterns = [
    path(r'v01_entrance/index', v01_entrance.IndexView.as_view(), name='ログイン画面'),
]
