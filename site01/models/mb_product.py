from django.db import models
from site01.extends.models import ModelHelperMixin

class MbProduct(models.Model, ModelHelperMixin):

    #id = models.BigAutoField()
    product_no = models.CharField(max_length=30)
    product_nm = models.CharField(max_length=100)
    delete_flg = models.BooleanField(blank=True, null=True, default=False)
    create_id = models.BigIntegerField(blank=True, null=True)
    create_ts = models.DateTimeField(auto_now_add=True)
    update_id = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return "{0}:{1}:{2}".format(self.id, self.product_no, self.product_nm)
        # return '%o.%o.%o.%o.%o.%o.%o.%o' % (self.id, self.product_no, self.product_nm
        #     , self.delete_flg, self.create_id, self.create_ts, self.update_id, self.update_ts)
        # return ', '.join(map(str, [self.id, self.product_no, self.product_nm
        #     , self.delete_flg, self.create_id, self.create_ts, self.update_id, self.update_ts]))
        # return super().to_str([self.id, self.product_no, self.product_nm
        #     , self.delete_flg, self.create_id, self.create_ts, self.update_id, self.update_ts])
        return super().to_str()

    class Meta:
        managed = False
        db_table = 'mb_product'
        app_label = 'site01' # 追加
