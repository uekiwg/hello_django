from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
#from django.views import View
from django import forms

#from manager.models import *
from site01.site.models.session import UserSession

"""
ログインビュー
"""
class IndexView(TemplateView):
    template_name = "s02_prod/v01_product.html"

    """
    GETメソッドで呼び出される
    """
    def get(self, request, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['methodName'] = 'get'
        context['user_session'] = UserSession.load(request.session)
        context['form'] = IndexForm()
        return render(request, self.template_name, context)

    """
    POSTメソッドで呼び出される
    """
    def post(self, request, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['methodName'] = 'post'
        form = IndexForm(request.POST)
        context['form'] = form
        if form.is_valid():
            context['methodName'] = 'post is valid'
        return render(request, self.template_name, context)

    def test(self, request, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['methodName'] = 'test'
        return render(request, self.template_name, context)

    # def get(self, request, *args, **kwargs):
    #     #context = super(WorkerListView, self).get_context_data(**kwargs)
    #     #return render(self.request, self.template_name, context)
    #     return render(self.request, self.template_name)

LANG_CHOICES = (('en', 'English'), ('ja', 'Japanese'))
class IndexForm(forms.Form):
    user_id = forms.CharField(label='User ID', max_length=50, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=50)
    lang = forms.ChoiceField(label='Language', widget=forms.Select, choices=LANG_CHOICES)
