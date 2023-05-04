"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""
from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, DATE
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True)
    username = Column(TEXT, nullable=False, unique=True)
    password = Column(TEXT, nullable=False)
    
    scheduled_classes = relationship("ScheduledClass", back_populates="user")

class ScheduledClass(Base):
    __tablename__ = "scheduled_classes"

    id = Column(INTEGER, primary_key=True)
    teacher = Column(TEXT, nullable=False)
    date = Column(DATE, nullable=False)
    user_id = Column(INTEGER, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="scheduled_classes")
    curriculums = relationship("Curriculum", back_populates="scheduled_class")

class Curriculum(Base):
    __tablename__ = "curriculums"

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)
    description = Column(TEXT)
    difficulty = Column(TEXT)
    language = Column(TEXT)
    scheduled_class_id = Column(INTEGER, ForeignKey('scheduled_classes.id'))
    
    scheduled_class = relationship("ScheduledClass", back_populates="curriculums")
