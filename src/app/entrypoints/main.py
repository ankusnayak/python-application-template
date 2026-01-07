from app.core.logging import logger
from app.config.settings import settings


def main() -> None:
    cfg = settings()
    logger.info("Starting %s in %s", cfg.app_name, cfg.env)


if __name__ == "__main__":
    main()
