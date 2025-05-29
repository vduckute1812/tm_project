from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper


class DatabaseWrapper(MySQLDatabaseWrapper):
    def get_new_connection(self, conn_params):
        return super().get_new_connection(conn_params)

    def create_cursor(self, name=None):
        return super().create_cursor(name)