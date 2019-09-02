from sqlalchemy import Table, Column, Integer, String, MetaData, Sequence, DateTime

metadata = MetaData()

users = Table('users', metadata,
   Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
   Column('name', String(50)),
   Column('email', String(50)),
   Column('created_at', DateTime),
   Column('updated_at', DateTime),
)