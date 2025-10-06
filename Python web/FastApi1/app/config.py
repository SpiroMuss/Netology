import os
from dotenv import load_dotenv
load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'Polygon')

PG_DSN = (f"postgresql+asyncpg://"
          f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
          f"{POSTGRES_HOST}:{POSTGRES_PORT}/"
          f"{POSTGRES_DB}")