from sqlalchemy import *
from migrate import *

metadata = MetaData()

users = Table('users', metadata,
   Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
   Column('name', String(50)),
   Column('email', String(50)),
   Column('created_at', DateTime),
   Column('updated_at', DateTime),
)

reminder = Table('reminder', metadata,
   Column('id', Integer, Sequence('reminder_id_seq'), primary_key=True),
   Column('reminder_when', DateTime),
)

reminder_users = Table('reminder_users', metadata,
   Column('reminder_id', ForeignKey("reminder.id"), nullable=False),
   Column('user_id', ForeignKey("users.id"), nullable=False),
)

def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    reminder_users.create()

def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    reminder_users.create()
