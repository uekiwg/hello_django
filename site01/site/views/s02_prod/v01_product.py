from django.shortcuts import render, redirect
from django import forms

from site01.site.views.extends import BaseView

#from manager.models import *

"""
ビュー
"""
class View(BaseView):

    #: テンプレート
    template_name = "s02_prod/v01_product.html"

    def get(self, request, *args, **kwargs):
        """
        GETメソッドで呼び出される
        """
        context = super().get_context_data(Form(), **kwargs)
        context['methodName'] = 'get'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        POSTメソッドで呼び出される
        """
        context = super().get_context_data(None, **kwargs)
        context['methodName'] = 'post'
        form = Form(request.POST)
        context['form'] = form
        if form.is_valid():
            context['methodName'] = 'post is valid'
        return render(request, self.template_name, context)

class Form(forms.Form):
    user_id = forms.CharField(label='User ID', max_length=50, required=True)

