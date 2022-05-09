import logging
format = "%(asctime)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
logging.basicConfig(
    format=format,
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level='INFO'
)

logger = logging.getLogger(__name__)
