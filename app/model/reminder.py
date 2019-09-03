from sqlalchemy import Table, Column, Integer, String, MetaData, Sequence, DateTime, ForeignKey

metadata = MetaData()

reminder = Table('reminder', metadata,
   Column('id', Integer, Sequence('reminder_id_seq'), primary_key=True),
   Column('reminder_when', DateTime),
)

reminder_users = Table('reminder_users', metadata,
   Column('reminder_id', ForeignKey("reminder.id"), nullable=False),
   Column('user_id', ForeignKey("users.id"), nullable=False),
)
