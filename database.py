from sqlalchemy import MetaData, create_engine, Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List, Optional
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin

from datetime import datetime, date


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)



class Users(UserMixin, db.Model):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]  
    password: Mapped[str]
    pushups: Mapped[List["Pushups"]] = relationship(back_populates="parent")

    def get_total(self):
        #total = sum(self.pushups) 
        #for pushup in self.pushups:
        #    total += pushup.number
        return(sum( [pushup.number for pushup in  self.pushups ] ))

    def get_daily_total(self):
        total = 0
        for pushup in self.pushups:
            if pushup.date.date() == datetime.today().date():
                total += pushup.number
        return(total)



class Pushups(UserMixin, db.Model):
    __tablename__ = "Pushups"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] 
    number: Mapped[int]
    parent_id: Mapped[int] = mapped_column( ForeignKey("Users.id") )
    parent: Mapped["Users"] = relationship( back_populates="pushups" ) 
