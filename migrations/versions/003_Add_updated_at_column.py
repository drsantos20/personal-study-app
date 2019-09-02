from sqlalchemy import *
from migrate import *

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    users = Table('users', meta, autoload=True)
    updated_atc = Column('updated_at', DateTime)
    updated_atc.create(users)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    users = Table('users', meta, autoload=True)
    users.c.updated_at.drop()
