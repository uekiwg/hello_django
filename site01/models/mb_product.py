from django.db import models
from site01.extends.models import ModelHelperMixin

class MbProduct(models.Model, ModelHelperMixin):

    #id = models.BigAutoField()
    product_no = models.CharField(max_length=30, verbose_name='')
    product_nm = models.CharField(max_length=100, verbose_name='')
    delete_flg = models.BooleanField(blank=True, null=True, default=False, verbose_name='')
    create_id = models.BigIntegerField(blank=True, null=True, verbose_name='')
    create_ts = models.DateTimeField(auto_now_add=True, verbose_name='')
    update_id = models.BigIntegerField(blank=True, null=True, verbose_name='')
    update_ts = models.DateTimeField(auto_now=True, verbose_name='')

    def __str__(self):
        return super().to_str()

    class Meta:
        managed = False
        db_table = 'mb_product'
        app_label = 'site01' # 追加
