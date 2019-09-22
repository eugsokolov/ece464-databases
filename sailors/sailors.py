'''
Sailors and Boats lecture script
@eugsokolov
'''
from __future__ import print_function
from ipdb import set_trace

from sqlalchemy import create_engine
engine = create_engine(
      "mysql+pymysql://eugene:@localhost/sailors?host=localhost?port=3306", echo=True)

conn = engine.connect()
print(conn.execute("SELECT * from sailors").fetchall())

set_trace()

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, DateTime
Base = declarative_base()

class Sailor(Base):
    __tablename__ = 'sailors'

    sid = Column(Integer, primary_key=True)
    sname = Column(String)
    rating = Column(Integer)
    age = Column(Integer)

    def __repr__(self):
        return "<Sailor(id=%s, name='%s', rating=%s)>" % (self.sid, self.sname, self.age)

tmp = Sailor(sid=98, sname='joe', rating=7, age=25)
print(tmp)

from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
s = session()

s.add(tmp)

set_trace()  # joe is "pending"

s.commit()

set_trace()

tmp.rating = 8
print('session is dirty?', s.dirty)

set_trace()

s.commit()

set_trace()

sailors = s.query(Sailor)
print(type(sailors), sailors)

set_trace()

for i in sailors:
    print(i)

set_trace()

from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref, relationship

class Boat(Base):
    __tablename__ = 'boats'

    bid = Column(Integer, primary_key=True)
    bname = Column(String)
    color = Column(String)
    length = Column(Integer)

    reservations = relationship('Reservation',
                                backref=backref('boat', cascade='delete'))

    def __repr__(self):
        return "<Boat(id=%s, name='%s', color=%s)>" % (self.bid, self.bname, self.color)

from sqlalchemy import PrimaryKeyConstraint

class Reservation(Base):
    __tablename__ = 'reserves'
    __table_args__ = (PrimaryKeyConstraint('sid', 'bid', 'day'), {})

    sid = Column(Integer, ForeignKey('sailors.sid'))
    bid = Column(Integer, ForeignKey('boats.bid'))
    day = Column(DateTime)

    sailor = relationship('Sailor')

    def __repr__(self):
        return "<Reservation(sid=%s, bid=%s, day=%s)>" % (self.sid, self.bid, self.day)

for i in s.query(Reservation):
    print(i)

set_trace()

