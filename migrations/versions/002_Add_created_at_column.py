from sqlalchemy import *
from migrate import *

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    users = Table('users', meta, autoload=True)
    created_atc = Column('created_at', DateTime)
    created_atc.create(users)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    users = Table('users', meta, autoload=True)
    users.c.created_at.drop()
