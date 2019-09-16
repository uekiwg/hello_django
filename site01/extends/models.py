from django.db import models

class ModelHelperMixin:
    def to_str(self):
        meta_fields = self._meta.get_fields()
        ret = dict()
        for i, meta_field in enumerate(meta_fields):
            ret[meta_field.name] = getattr(self, meta_field.name)
        return str(ret)
