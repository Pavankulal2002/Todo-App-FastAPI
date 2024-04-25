from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://Pavan:pavan_123@localhost:3306/todo_fastapi")

meta = MetaData()

conn = engine.connect()