from logging import getLogger
from django.shortcuts import render, redirect
from django import forms

from site01.views.extends import BaseView
from site01.models import MaUser, MbProduct
from site01.utils.debug import TraceUtil

logger = getLogger(__name__)

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
        # print("-----------------------------0")
        # TraceUtil.printQuery()
        # print("-----------------------------1")
        context['product_list'] = MbProduct.objects.all()
        # TraceUtil.printQuery()
        # print("-----------------------------2")
        # print(str(context['product_list']))

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        POSTメソッドで呼び出される
        """
        context = super().get_context_data(Form(request.POST), **kwargs)
        context['methodName'] = 'post'
        context['product_list'] = MbProduct.objects.filter()
        TraceUtil.printQuery()
        print(str(context['product_list']))
        return render(request, self.template_name, context)

class Form(forms.Form):
    user_id = forms.CharField(label='User ID', max_length=50, required=True)

