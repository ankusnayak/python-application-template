import logging
from app.config.settings import settings

cfg = settings()

logging.basicConfig(
    level=cfg.log_level,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)

logger = logging.getLogger(cfg.app_name)
