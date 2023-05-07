"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""
from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, DATE
from sqlalchemy.orm import relationship
from database import Base

# Define the User class, which corresponds to the "users" table in the database
class User(Base):
    __tablename__ = "users"

    # Define the columns for the User table
    id = Column(INTEGER, primary_key=True)
    username = Column(TEXT, nullable=False, unique=True)
    password = Column(TEXT, nullable=False)
    
    # Define a one-to-many relationship between User and ScheduledEvents
    scheduled_classes = relationship("ScheduledEvents", back_populates="user")

# Define the ScheduledEvents class, which corresponds to the "scheduled_classes" table in the database
class ScheduledEvents(Base):
    __tablename__ = "scheduled_classes"

    # Define the columns for the ScheduledEvents table
    id = Column(INTEGER, primary_key=True)
    title = Column(TEXT, nullable=False)
    date = Column(DATE, nullable=False)
    user_id = Column(INTEGER, ForeignKey('users.id'))
    
    # Define a many-to-one relationship between ScheduledEvents and User
    user = relationship("User", back_populates="scheduled_classes")
