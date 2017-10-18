#!/usr/bin/env python
import MySQLdb


class DB(object):
    def __init__(self, db_params):
        self.host = db_params['host']
        self.port = db_params['port']
        self.user = db_params['user']
        self.password = db_params['password']
        self.db_name = db_params['db_name']
        self.connection = MySQLdb.Connection(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.db_name
        )
        self.dbh = self.connection.cursor()

    def query(self, query_string):
        self.dbh.execute(query_string)
        return self.dbh.fetchall()
