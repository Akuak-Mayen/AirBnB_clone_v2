#!/usr/bin/python
"""
    This is the User module, which defines the User class.
    The User class represents new users and holds information about them.
"""

from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel):
    """User representation"""
  __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='user')

    reviews = relationship('Review', cascade='all, delete, delete-orphan',
                           backref='user')

    def __init__(self, *args, **kwargs):
        """User initialization"""
        super().__init__(*args, **kwargs)
