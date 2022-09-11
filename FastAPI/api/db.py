
from sqlalchemy import (
    Column,
    Integer,
    FLOAT,
    MetaData,
    String,
    Table,
    create_engine
)

from databases import Database
import pymysql
from .connect import sql, user, password, host, db


pymysql.install_as_MySQLdb()
DATABASE_URL = SQLALCHEMY_DATABASE_URL = (rf"{sql}://{user}:{password}@{host}/{db}")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

Info = Table(
    "Client",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("user_name", String(100)),
    Column("wallet_number", String(50)),
    Column("nickname", String(50), unique=True),
    Column("balance", FLOAT)

)

User = Table(
    "user",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("username", String(100), unique=True),
    Column("password", String(200)),

)

database = Database(DATABASE_URL)

