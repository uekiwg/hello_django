from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.conf import settings

from site01.site.views.extends import BaseView
from site01.site.models.sessions import UserSession
from site01.site.models.test import TestModel

"""
ログインビュー
"""
class View(BaseView):

    #: テンプレート
    template_name = "s01_comn/v01_entrance.html"

    def get(self, request, *args, **kwargs):
        """
        GETメソッドで呼び出される。
        """
        test = TestModel()
        print("test=" + test.test())

        # セッションクリア、クッキー削除
        request.session.clear()
        request.session.flush()

        # コンテキスト取得
        context = super().get_context_data(Form(request.GET or None), **kwargs)
        context['methodName'] = 'get'

        # 画面表示
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        POSTメソッドで呼び出される。
        """

        # コンテキスト取得
        context = super().get_context_data(Form(request.POST), **kwargs)
        context['methodName'] = 'post'
        form = context['form']
        
        # バリデーション
        if not form.is_valid():
            context['methodName'] = 'post is in valid'
            return render(request, self.template_name, context)

        # セッションへログイン情報を保存
        UserSession.create(request, form.cleaned_data)
        
        # 画面遷移
        return HttpResponseRedirect('/s02_prod/v01_product')

"""
ログインフォーム
"""
class Form(forms.Form):
    #: ユーザID
    user_id = forms.CharField(label='User ID', max_length=50, required=True)
    #: パスワード
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=50, required=False)
    #: 言語
    lang = forms.ChoiceField(label='Language', widget=forms.Select, choices=settings.LANGUAGES)
