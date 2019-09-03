from sqlalchemy import *
from migrate import *

metadata = MetaData()

activity_type = Table('activity_type', metadata,
   Column('id', Integer, Sequence('activity_type_seq'), primary_key=True),
   Column('name', String(50)),
)

def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    activity_type.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    activity_type.drop()


