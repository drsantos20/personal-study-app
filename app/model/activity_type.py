from sqlalchemy import Table, Column, Integer, String, MetaData, Sequence, DateTime, ForeignKey

metadata = MetaData()

activity_type = Table('activity_type', metadata,
   Column('id', Integer, Sequence('activity_type_seq'), primary_key=True),
   Column('name', String(50)),
)