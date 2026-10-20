import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "probatalog.txt"

def setup_logging() -> None:
	formatter = logging.Formatter(
		fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
		datefmt="%Y-%m-%d %H:%M:%S",
	)

	file_handler = RotatingFileHandler(
		LOG_FILE,
		maxBytes=5 * 1024 * 1024, # 5mb
		backupCount=5, # max no of backups before cycling
		encoding="utf-8"
	)
	file_handler.setFormatter(formatter)

	logging.basicConfig(
		level=logging.INFO,
		handlers=[file_handler],
		force=True,
	)