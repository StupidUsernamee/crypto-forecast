from typing_extensions import Self
import psycopg2 as postgre
from threading import Lock

class DatabaseConnector:
    _instance = None
    _lock = Lock()

    def __new__(cls, host: str, db: str, user: str, password: str):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._init_connection(host, db, user, password)

    def _init_connection(self, host: str, db: str, user: str, password: str):
        self.conn = postgre.connect(
            host=host, dbname=db, user=user, password=password
        )
        self.cursor = self.conn.cursor()