from sqlalchemy import MetaData, create_engine, Column, String, Integer
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List, Optional
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)



class Users(UserMixin, db.Model):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]  
    password: Mapped[str]
    number: Mapped[int]
