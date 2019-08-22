'''
Sailors and Boats lecture script
@eugsokolov
'''

from ipdb import set_trace

from sqlalchemy import create_engine
engine = create_engine(
      "mysql+pymysql://eugene:@localhost/sailors?host=localhost?port=3306", echo=True)

conn = engine.connect()
print conn.execute("SELECT * from sailors").fetchall()

set_trace()

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
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
print tmp

set_trace()

from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
s = session()
sailors = s.query(Sailor)
print type(sailors), sailors
set_trace()

for i in sailors:
    print i

set_trace()
