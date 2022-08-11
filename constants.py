from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent

INIT_DATA_DIR: Path = BASE_DIR.joinpath('init_data')

DATA_JSON: Path = INIT_DATA_DIR.joinpath('data.json')
