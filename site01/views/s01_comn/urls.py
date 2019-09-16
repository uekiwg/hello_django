from django.urls import path

from . import v01_entrance

urlpatterns = [
    path(r'v01_entrance', v01_entrance.View.as_view(), name='ログイン画面'),
]
