
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
	               , Column('user_id', Integer, ForeignKey('user.idg'))
	               , Column('email_address', String, nullable=False))

# table create
metadata.create_all(engine)


# db연결
conn = engine.connect()


# insert 예제 #1
ins = users.insert();
print(str(ins))
ins = users.insert().values(id=1, name='Jack', fullname='Jack Jones')
ins.compile().params
result = conn.execute(ins)
print(result, '건 인서트')
print()

#insert 예제 #2
ins = users.insert()
result = conn.execute(ins,  id=2, name='Wendy', fullname='Wendy William')
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

# select 예제
# 전체 다 select
print('users 테이블 출력')
s = select([users])
rslt = conn.execute(s)
for row in rslt:
	print(row)

print()
print('addresses 테이블 출력')
s = select([addresses])
rslt = conn.execute(s)
for row in rslt:
	print(row)

print('addresses 테이블 한줄만 출력')
s = select([users])
rslt = conn.execute(s)
row = rslt.fetchone()

print(row[0], row[1], row[2])
print(row['id'], row['name'], row['fullname'])
print()
print('특정필드만 추출')

s = select([users.c.id, users.c.fullname])
rslt = conn.execute(s)
for row in rslt:
	print(row)

#두개 테이블 다 추출 및 조인
s = select([users.c.id, addresses.c.email_address]).where(users.c.id == addresses.c.user_id)
rslt = conn.execute(s)
for row in rslt:
	print(row)









