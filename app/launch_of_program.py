import logging
import tomllib
import logging

from pathlib import Path

def load_config() -> dict[str, str]:
    with open("config.toml", "rb") as file:
        return tomllib.load(file)

def determine_directory_of_database():
    config = load_config()
    PROJECT_DIR = Path(__file__).resolve().parent.parent

    DATA_DIR = PROJECT_DIR / config["database"]["database_directory"]
    DATABASE_FILE = DATA_DIR / config["database"]["database_file"]

    return DATABASE_FILE

def create_log_file():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d.%m.%Y %H:%M:%S",
        encoding="utf-8"
    )