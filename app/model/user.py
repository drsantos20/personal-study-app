from sqlalchemy import Table, Column, Integer, String, MetaData, Sequence

metadata = MetaData()

users = Table('users', metadata,
   Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
   Column('name', String(50)),
   Column('email', String(50)),
)