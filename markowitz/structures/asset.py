# Dependencies
# ----------------------------------------------------------------------------------------------------------
import sqlite3

# Headers
# ----------------------------------------------------------------------------------------------------------
from .module_header import m_types, m_maths, m_structs, m_utils


# Database Handling
# ----------------------------------------------------------------------------------------------------------
class m_DB_Connection(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.cnx = sqlite3.connect(file_name)

    def __enter__(self):
        return self.cnx

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cnx.close()
        print("Exiting Connection: " + self.file_name)
        return 0


# Public API
# ----------------------------------------------------------------------------------------------------------
class m_Asset(m_structs.A_TYPE):
    _data_col = "clot"

    @classmethod
    def load_sql(cls, con: sqlite3.Connection, name: str) -> m_types.A_TYPE:
        main_df = m_utils.read_sql_query(
                "SELECT * FROM {}".format(name.upper()),
                con)

        df_var: m_structs.DataFrame = main_df[m_Asset._data_col].pct_change()
        return cls(name, df_var, df_var.mean(), m_maths.sqrt(df_var.var()))

    def __init__(self, name: str, df, mu: float, sigma: float) -> None:
        self.name: str = name
        self.avg: float = m_types.M_FLOAT(mu)
        self.stdv: float = m_types.M_FLOAT(sigma)
        self.df: m_structs.DataFrame = df

    def __repr__(self) -> str:
        return "<Titre: {name} | {lenght} | {avg} | {stdv}>".format(
                name=self.name,
                lenght=len(self.df),
                avg=self.avg,
                stdv=self.stdv
            )
