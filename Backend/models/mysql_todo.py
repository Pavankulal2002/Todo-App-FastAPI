from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from databases.mysql import meta, engine

todos = Table(
    "todos",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "name",
        String(255),
    ),
    Column("description", String(255)),
)

meta.create_all(engine)
