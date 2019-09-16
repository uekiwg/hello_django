from django.db import models

class ModelHelperMixin:
    def to_str(self):
        # return ', '.join(map(str, fields))
        # return str(self._meta.fields)
        meta_fields = self._meta.get_fields()
        # ret = list()
        # for i, meta_field in enumerate(meta_fields):
        #     if i > 0:
        #         ret.append(meta_field.name + "getattr(obj, 'field_name')")
        ret = dict()
        for i, meta_field in enumerate(meta_fields):
            ret[meta_field.name] = getattr(self, meta_field.name)
        return str(ret)

# class BaseModel(models.Model):
#     testaaa = ""
    # delete_flg = models.BooleanField(blank=True, null=True, default=False)
    # create_id = models.BigIntegerField(blank=True, null=True)
    # create_ts = models.DateTimeField(auto_now_add=True)
    # update_id = models.BigIntegerField(blank=True, null=True)
    # update_ts = models.DateTimeField(auto_now=True)
    # def to_string(self, fields):
    #     return ', '.join(map(str, [fields
    #         , self.delete_flg, self.create_id, self.create_ts, self.update_id, self.update_ts]))
