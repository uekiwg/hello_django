
from django.views.generic import TemplateView

from site01.site.models.sessions import UserSession

class BaseView(TemplateView):
    def get_context_data(self, form, **kwargs):
        """
        TemplateView#get_context_data をオーバライド
        """
        context = super().get_context_data(**kwargs)

        # コンテキストへオブジェクトを追加
        context['user_session'] = self.get_user_session(self.request)
        context['form'] = form

        return context

    def get_user_session(self, request):
        return UserSession.load(request.session)

