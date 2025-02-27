from sqlalchemy import MetaData, create_engine, Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List, Optional
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin

from datetime import datetime, date


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def is_today(obj):
    return( obj.date.date() == datetime.today().date())


class Users(UserMixin, db.Model):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]  
    password: Mapped[str]
    pushups: Mapped[List["Pushups"]] = relationship(back_populates="parent")
    team_id: Mapped[int] = mapped_column( ForeignKey("Team.id") )
    team: Mapped["Team"] = relationship( back_populates="users" ) 

    def get_total(self):
        return(sum( [pushup.number for pushup in  self.pushups ] ))

    def get_daily_total(self):
      return( sum( [ pushup.number for pushup in  list( filter(  is_today, self.pushups ) ) ] ))


class Pushups(UserMixin, db.Model):
    __tablename__ = "Pushups"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] 
    number: Mapped[int]
    parent_id: Mapped[int] = mapped_column( ForeignKey("Users.id") )
    parent: Mapped["Users"] = relationship( back_populates="pushups" ) 


class Team(UserMixin, db.Model):
    __tablename__ = "Team"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    total: Mapped[int]
    users: Mapped[Optional[List["Users"]]] = relationship(back_populates="team")

    def get_total(self):
        self.total = sum( [ user.get_total() for user in self.users ] )
