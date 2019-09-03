from sqlalchemy import Table, Column, Integer, String, MetaData, Sequence, DateTime, ForeignKey

metadata = MetaData()

activity = Table('activity', metadata,
   Column('id', Integer, Sequence('activity_seq'), primary_key=True),
   Column('description', String(50)),
   Column('activity_id', Integer, ForeignKey("activity_type.id"), nullable=False),
)

activity_users = Table('activity_users', metadata,
   Column('activity_id', ForeignKey("activity.id"), nullable=False),
   Column('user_id', ForeignKey("users.id"), nullable=False),
)