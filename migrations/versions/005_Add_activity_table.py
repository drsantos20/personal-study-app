from sqlalchemy import *
from migrate import *

metadata = MetaData()

activity_type = Table('activity_type', metadata,
   Column('id', Integer, Sequence('activity_type_seq'), primary_key=True),
   Column('name', String(50)),
)

activity = Table('activity', metadata,
   Column('id', Integer, Sequence('activity_seq'), primary_key=True),
   Column('description', String(50)),
   Column('activity_type_id', Integer, ForeignKey("activity_type.id"), nullable=False),
)

def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    activity.create()

def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    activity.drop()

