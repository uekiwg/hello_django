from logging import getLogger
from django.contrib import admin
from .models import MaUser, MbProduct

logger = getLogger(__name__)

logger.info("admin.site.register MaUser, MbProduct")
admin.site.register(MaUser)
admin.site.register(MbProduct)
