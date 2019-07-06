import pandas as pd
from os import listdir
import sqlite3 as s3


xlsx_path = "CAC40"


class Tableau(object):
    def __init__(self, file, data):
        self.file = file
	self.data = data

    def __repr__(self):
	return "<Tableau file: " + self.file + "; data_len: " + str(len(self.data)) + ">"

    @property
    def title(self):
	return self.file[:-5]

    def sql_table(self, cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
	    idx INT PRIMARY KEY,
	    isin VARCHAR(12),
	    jour DATE,
	    ouvr FLOAT(3,3),
	    phaut FLOAT(3,3),
	    pbas FLOAT(3,3),
	    clot FLOAT(3,3),
	    volume INT
	)""".format(self.title))
	
        return self


    def fmt_time(self):
	self.data['JOUR'] = self.data['JOUR'].dt.strftime('%Y-%m-%d')
	return self

    def sql_write_lines(self, cursor):
        for i in range(len(self.data)):
            sqline = list(self.data.iloc[i])
            sqline.insert(0, i)
            sqline.insert(0, self.title)
            if self.title == "CAC40":
                query = "INSERT INTO %s(idx, isin, jour, ouvr, phaut, pbas, clot) VALUES (%i, '%s', '%s', %f, %f, %f, %f)" % tuple(sqline)
            else:
                query = "INSERT INTO %s VALUES (%i, '%s', '%s', %f, %f, %f, %f, %i)" % tuple(sqline)
            cursor.execute(query)
        return self



def main():
    tables = list(
        map(lambda x: x.fmt_time(),
            [
                Tableau(file, pd.read_excel(xlsx_path + '/' + file)) 
                for file in listdir(xlsx_path) 
                if ".xlsx" in file and file[0] != "#"
            ]
        )
    )
    
    conn = s3.connect('cac40.db')
    c = conn.cursor()
    for table in tables:
	table.sql_table(c)
	print(table.file)
	table.sql_write_lines(c) 
    c.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
	main()
