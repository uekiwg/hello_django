from django.db import models

class MaUser(models.Model):
    #id = models.TextField()  # This field type is a guess.
    user_id = models.CharField(max_length=30)
    user_nm = models.CharField(max_length=30)
    lang = models.CharField(max_length=2, blank=True, null=True)
    delete_flg = models.BooleanField(blank=True, null=True, default=False)
    create_id = models.BigIntegerField(blank=True, null=True)
    create_ts = models.DateTimeField()
    update_id = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ma_user'
        app_label = 'site01' # 追加

