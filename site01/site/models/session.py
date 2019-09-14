"""
ユーザセッション
"""
class UserSession():
    KEY = 'user_session__'
    __data = {}

    def __init__(self, data):
        self.__data = data

    @classmethod
    def load(cls, session):
        """
        ユーザセッションを作成する。
        """
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
