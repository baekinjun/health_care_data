from dbutils.pooled_db import PooledDB
from config import Database_config
import urllib3
import psycopg2

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DB = PooledDB(
    ping=7,
    creator=psycopg2,
    mincached=5,
    blocking=True,
    host=Database_config['host'],
    port=Database_config['port'],
    user=Database_config['user'],
    password=Database_config['Password'],
    database=Database_config['Database'],
)