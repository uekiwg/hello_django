from logging import getLogger
from django.apps import AppConfig

logger = getLogger(__name__)

class Site01Config(AppConfig):
    name = 'site01'

    def ready(self):
        logger.info("Site01Config#ready.")
