"""
ユーザセッション
"""
class UserSession():
    KEY = 'user_session__'
    __data = {}

    def __init__(self, data):
        self.__data = data

    @classmethod
    def create(cls, request, data):
        """
        ユーザセッションを作成する。
        """
        request.session[cls.KEY] = {
            'user_id': data['user_id'], 
            'lang':    data['lang']
        }

    @classmethod
    def load(cls, session):
        """
        ユーザセッションをロードする。
        """
        if session is None or not cls.KEY in session:
            return None
        return UserSession(session[cls.KEY])

    @property
    def user_id(self):
        """
        ユーザID を取得する。
        """
        return self.__data['user_id']

    @property
    def lang(self):
        """
        言語 を取得する。
        """
        return self.__data['lang']
