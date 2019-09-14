from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
#from django.views import View
from django.http import HttpResponseRedirect
from django import forms

from site01.site.models.session import UserSession
#from manager.models import *

"""
ログインビュー
"""
class IndexView(TemplateView):
    """
    ログイン機能を実装シータクラス。
    """

    #: デフォルトのテンプレート
    template_name = "s01_comn/v01_entrance.html"

    def get(self, request, *args, **kwargs):
        """
        GETメソッドで呼び出される。
        """

        # request.session.clear()
        request.session.clear()

        # セッションとクッキーを削除
        request.session.flush()

        context = super(IndexView, self).get_context_data(**kwargs)
        context['methodName'] = 'get'
        context['form'] = IndexForm(request.GET or None)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        POSTメソッドで呼び出される。
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['methodName'] = 'post'
        form = IndexForm(request.POST)
        context['form'] = form
        if not form.is_valid():
            context['methodName'] = 'post is valid'
        #return render(request, self.template_name, context)

        # セッションにデータを保存
        # request.session['user_session'] = UserSession(
        #     form.cleaned_data['user_id'], 
        #     form.cleaned_data['lang']
        # )
        request.session[UserSession.KEY] = {
            'user_id': form.cleaned_data['user_id'], 
            'lang':    form.cleaned_data['lang']
        }
        
        # 画面遷移
        return HttpResponseRedirect('/s02_prod/v01_product/index')

#: 言語一覧
LANG_CHOICES = (('en', 'English'), ('ja', 'Japanese'))

"""
ログインフォーム
"""
class IndexForm(forms.Form):
    #: ユーザID
    user_id = forms.CharField(label='User ID', max_length=50, required=True)
    #: パスワード
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=50, required=False)
    #: 言語
    lang = forms.ChoiceField(label='Language', widget=forms.Select, choices=LANG_CHOICES)
