""" Script to create a SQLite database from a directory of CAC40 historic data excel sheets """
from os import listdir
import sqlite3 as s3
import pandas as pd


class Table:
    """Representation of an excel table loaded into
       a pandas dataframe to be inserted in a SQLite database
    """

    def __init__(self, file, data):
        self.file = file
        self.data = data

    def __repr__(self):
        return (
            "<Tableau file: " + self.file + "; data_len: " + str(len(self.data)) + ">"
        )

    @property
    def title(self):
        """ name of the file """
        return self.file[:-5]

    def make_table(self, cursor):
        """ Create the table if needed """
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.title} (
idx INT PRIMARY KEY,
isin VARCHAR(12),
jour DATE,
ouvr FLOAT(3,3),
phaut FLOAT(3,3),
pbas FLOAT(3,3),
clot FLOAT(3,3),
volume INT
)"""
        )
        return self

    def fmt_time(self):
        """ format time for specific table """
        self.data["JOUR"] = self.data["JOUR"].dt.strftime("%Y-%m-%d")
        return self

    def write_lines(self, cursor):
        """ write all lines to database """
        for i in range(len(self.data)):
            sqline = list(self.data.iloc[i])
            sqline.insert(0, i)
            sqline.insert(0, self.title)
            if self.title == "CAC40":
                query = "INSERT INTO %s(idx, isin, jour, ouvr, phaut, pbas, clot)" % sqline[
                    0
                ] + "VALUES (%i, '%s', '%s', %f, %f, %f, %f)" % tuple(
                    sqline[1:]
                )
            else:
                query = (
                    "INSERT INTO %s VALUES (%i, '%s', '%s', %f, %f, %f, %f, %i)"
                    % tuple(sqline)
                )
            cursor.execute(query)
        return self


def connect(database):
    """ Decorator to handle database connection """

    def decorator(func):
        def wrapper(*args, **kwargs):
            conn = s3.connect(database)
            cursor = conn.cursor()
            kwargs["cursor"] = cursor
            ret = func(*args, **kwargs)
            cursor.close()
            conn.commit()
            conn.close()
            return ret

        return wrapper

    return decorator


@connect("cac40.db")
def main(path: str, cursor: object = None):
    """ Transpose excel tables in a sqlite database """
    tables = map(
        lambda x: x.fmt_time(),
        [
            Table(file, pd.read_excel(path + "/" + file))
            for file in listdir(path)
            if ".xlsx" in file and file[0] != "#"
        ],
    )
    for table in tables:
        print(table.file)
        table.make_table(cursor).write_lines(cursor)


if __name__ == "__main__":
    main("CAC40")
