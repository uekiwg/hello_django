from django.db import connection, reset_queries

class TraceUtil:
    @classmethod
    def printQuery(cls):
        for history in connection.queries:
            print(history)
        reset_queries()

