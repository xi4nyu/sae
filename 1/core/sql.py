#-*- coding:utf-8 -*-

from MySQLdb import connect

try:
    from sae.const import MYSQL_DB, MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_HOST_S
except:
    from setting import MYSQL_DB, MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_HOST_S


CREATE_BLOG = """
    CREATE TABLE IF NOT EXISTS blog
    (
        id int auto_increment not null,
        title varchar(50) not null,
        content text not null,
        create_time timestamp not null,
        is_show boolean not null,
        primary key(id)
    )
"""

CREATE_USER = """
    CREATE TABLE IF NOT EXISTS user
    (
        id int auto_increment not null,
        user_name varchar(50) not null,
        password char(32) not null,
        is_admin boolean not null,
        primary key(id)
    )
"""
ADMIN_USER = """
    insert into user(user_name, password, is_admin) values('llq17501', 'e10adc3949ba59abbe56e057f20f883e', 1);
"""

CREATE_TODO = """
    CREATE TABLE IF NOT EXISTS todo
    (
        id int auto_increment not null,
        text varchar(255) not null,
        status int not null,
        primary key(id)
    )
"""
class DBHelper(object):
    def __init__(self):
        self.conn = connect(host = MYSQL_HOST, user = MYSQL_USER, passwd = MYSQL_PASS, port = MYSQL_PORT)
        self.conn.select_db(MYSQL_DB)
        self._init()

    def _init(self):
        cursor = self.conn.cursor()
        cursor.execute(CREATE_BLOG)
        cursor.execute(CREATE_USER)

    def find(self, sql):
        cursor = self.conn.cursor()
        count = cursor.execute(sql)
        result = cursor.fetchall()
        return count, result

    def find_one(self, sql, *value):
        cursor = self.conn.cursor()
        count = cursor.execute(sql, *value)
        if count:
            result = cursor.fetchone()
            return result

    def insert(self, table_name, column_names, values):
        cursor = self.conn.cursor()
        sql = "INSERT INTO {table_name}({column_names}) values({values})".format(table_name = table_name, column_names = ",".join(column_names), values = ",".join(["%s" for i in column_names]))
        n = cursor.executemany(sql, values)
        return n


