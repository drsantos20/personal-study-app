from sqlalchemy import *
from migrate import *

metadata = MetaData()

users = Table('users', metadata,
   Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
   Column('name', String(50)),
   Column('email', String(50)),
)

def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    users.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    users.drop
