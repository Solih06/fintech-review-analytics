import os
import logging
import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import execute_values
from dotenv import load_dotenv  # Import env configuration loader

# Configure clean terminal logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dynamically load values from the hidden local .env file
load_dotenv()

DB_USER = "postgres"
DB_PASSWORD = os.getenv("DB_PASSWORD")  # Secures password via variable reference
DB_HOST = "localhost"
DB_PORT = "5432"

if not DB_PASSWORD:
    logging.error("Security Halt: DB_PASSWORD not detected. Verify your local .env file contains it.")
    exit(1)

# The rest of your populate_database() functions remain exactly the same...