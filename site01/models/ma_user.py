from django.db import models
from site01.extends.models import ModelHelperMixin

class MaUser(models.Model, ModelHelperMixin):
    #id = models.BigAutoField()
    user_id = models.CharField(max_length=30)
    user_nm = models.CharField(max_length=30)
    lang = models.CharField(max_length=2, blank=True, null=True)
    delete_flg = models.BooleanField(blank=True, null=True, default=False)
    create_id = models.BigIntegerField(blank=True, null=True)
    create_ts = models.DateTimeField()
    update_id = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField()

    def __str__(self):
        return super().to_str()

    class Meta:
        managed = False
        db_table = 'ma_user'
        app_label = 'site01' # 追加

