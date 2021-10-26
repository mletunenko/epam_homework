import sqlite3 as sq


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def __getitem__(self, item):
        with sq.connect(self.database_name) as connect:
            self.connection = connect
            cursor = self.connection.cursor()
            request = f'SELECT age FROM {self.table_name} ' \
                      f'WHERE name = :pres_name'
            return cursor.execute(request, {'pres_name': item}).fetchone()[0]

    def __len__(self):
        with sq.connect(self.database_name) as connect:
            cursor = connect.cursor()
            return (
                cursor.execute(
                    f'SELECT COUNT(*) FROM {self.table_name}').fetchone()[
                    0])

    def __iter__(self):
        with sq.connect(self.database_name) as connect:
            self.connection = connect
            self.cursor = self.connection.cursor()
            sql_request = f'SELECT * FROM {self.table_name}'
            self.cursor.execute(sql_request)
            column_name_list = []
            for column in self.cursor.description:
                column_name_list.append(column[0])
            self.column_names = column_name_list
            return self

    def __next__(self):
        row = self.cursor.fetchone()
        if row is None:
            self.cursor.close()
            raise StopIteration
        return dict(zip(self.column_names, row))
