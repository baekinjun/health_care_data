from psycopg2.extras import RealDictCursor
from .db_postgre import DB
import logging
from common import dict_encoder
class Procedure:
    def __init__(self):
        self.conn = DB.connection()
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    @dict_encoder
    def b_fetchone(self, sql, args=()):
        try:
            self.cursor.execute(sql, args)
            rs = self.cursor.fetchone()
        except Exception as e:
            logging.error(e)
        return rs

    @dict_encoder
    def b_fetchall(self, sql, args=()):
        try:
            self.cursor.execute(sql, args)
            rs = self.cursor.fetchall()
        except Exception as e:
            logging.error(e)
        return rs

    @dict_encoder
    def b_execute(self, sql, args=()):
        try:
            self.cursor.execute(sql, args)
            self.cursor.execute("SELECT @o_out_code;")
            row = self.cursor.fetchone()
            rs = row['@o_out_code']
        except Exception as e:
            logging.error(e)
        return rs
