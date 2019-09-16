import logging
from django.apps import AppConfig

logger = logging.getLogger(__name__)

class PollsConfig(AppConfig):
    name = 'polls'

    def ready(self):
        logger.info("PollsConfig#ready.")
