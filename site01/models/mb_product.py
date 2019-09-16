from django.db import models

class MbProduct(models.Model):
    #id = models.TextField()  # This field type is a guess.
    product_no = models.CharField(max_length=30)
    product_nm = models.CharField(max_length=100)
    delete_flg = models.BooleanField(blank=True, null=True, default=False)
    create_id = models.BigIntegerField(blank=True, null=True)
    create_ts = models.DateTimeField()
    update_id = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField()

    def __str__(self):
        return "{0}:{1}:{2}".format(self.id, self.product_no, self.product_nm)
        
    class Meta:
        managed = False
        db_table = 'mb_product'
        app_label = 'site01' # 追加
