# import psycopg2

from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, String, DateTime, SmallInteger

#conn_string = "postgresql://jfine:uni1cast@192.168.1.25:5432/unidata"

conn_string = "postgresql://uni_pool:test_smccarter@192.1.25.5432/"
db = create_engine(conn_string)

# db.execute("INSERT INTO part_cast VALUES (now(), 'ANOTHER_PN', '99998F', 45)")

#meta = MetaData(db)  
'''
shell_table = Table('part_cast', meta,  
                        Column('pn',     String),
                        Column('lot',    String),
                        Column('hanger', SmallInteger))

with db.connect() as conn:
    insert_statement = shell_table.insert().values(pn="BigPart", lot="11111", hanger=1)
    conn.execute(insert_statement)

'''
result_set = db.execute("SELECT * FROM part_cast")
for r in result_set:  
    print(r)

