#Conjunction
# We’d like to show off some of our operators inside of select() constructs. 
# But we need to lump them together a little more, so let’s first introduce some conjunctions. 
# Conjunctions are those little words like AND and OR that put things together. 
# We’ll also hit upon NOT. and_(), or_(), and not_() can work from the corresponding functions SQLAlchemy provides (notice we also throw in a like()):
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy import select

# engine 초기화
engine = create_engine('sqlite:///:memory:', echo=True)

# Metadata object 생성
metadata = MetaData()

# users 테이블 생성
users = Table('user', metadata
	            , Column('id', Integer, primary_key=True)
	            , Column('name', String)
	            , Column('fullname', String))

# users 테이블 생성
addresses = Table('address', metadata
	               , Column('id', Integer, primary_key=True)
	               , Column('user_id', Integer, ForeignKey('user.id'))
	               , Column('email_address', String, nullable=False))

# table create
metadata.create_all(engine)


# db연결
conn = engine.connect()


# insert 예제 #1
ins = users.insert();
print(str(ins))
ins = users.insert().values(id=1, name='jack', fullname='Jack Jones')
ins.compile().params
result = conn.execute(ins)
print(result, '건 인서트')
print()

#insert 예제 #2
ins = users.insert()
result = conn.execute(ins,  id=2, name='wendy', fullname='Wendy William')
print(result, '건 인서트')
print()

#insert 예제 #3 - multi row
ins = addresses.insert()
result = conn.execute(ins, [{'id':1, 'user_id':1, 'email_address':'jack@gmail.com'}
	                      , {'id':2, 'user_id':1, 'email_address':'jack@yahoo.com'}
	                      , {'id':3, 'user_id':2, 'email_address':'wendy@gmail.com'}
	                      , {'id':4, 'user_id':2, 'email_address':'wendy@yahoo.com'}	                      	                       
	])
print(result, '건 인서트')
print()

from sqlalchemy.sql import and_, or_, not_

# Conjungtion을 이용한 select 
s = select([(users.c.fullname + ', ' + addresses.c.email_address).label('title')]).\
            where(
            	   and_(
            	   	      users.c.id == addresses.c.user_id, 
            	   	      users.c.name.between('m', 'z'),
                          or_(
                          	   addresses.c.email_address.like('%yahoo%'), 
                          	   addresses.c.email_address.like('%gmail%')
                          	  )
                        )
            	 )
rslt = conn.execute(s).fetchall()
print(rslt)



