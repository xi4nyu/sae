#-*- coding:utf-8 -*-

from MySQLdb import connect

try:
    from sae.const import MYSQL_DB, MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_HOST_S
except:
    from setting import MYSQL_DB, MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_HOST_S


CREATE_BLOG = """
    CREATE TABLE IF NOT EXISTS blog
    (
        id int,
        title char(40),
        content text,
        create_time timestamp,
        is_show boolean,
    )
"""
class DBHelper(object):
    def __init__(self):
        self.conn = connect(host = MYSQL_HOST, user = MYSQL_USER, passwd = MYSQL_PASS, port = MYSQL_PORT)
        self.conn.select_db(MYSQL_DB)

    def _init(self):
        cursor = self.conn.cursor()
        cursor.execute(CREATE_BLOG)

    def find(self, sql):
        cursor = self.conn.cursor()
        count = cursor.execute(sql)
        result = cursor.fetchall()
        return count, result

    def find_one(self, sql):
        cursor = self.conn.cursor()
        count = cursor.excute(sql)
        if count:
            result = cursor.fetchone()
            return result
        else:
            return None
