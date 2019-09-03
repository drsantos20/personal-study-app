from sqlalchemy import *
from migrate import *

metadata = MetaData()

reminder = Table('reminder', metadata,
   Column('id', Integer, Sequence('reminder_id_seq'), primary_key=True),
   Column('reminder_when', DateTime),
)

users = Table('users', metadata,
   Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
   Column('name', String(50)),
   Column('email', String(50)),
   Column('created_at', DateTime),
   Column('updated_at', DateTime),
)

def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    reminder.create()

def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    reminder.drop()

