import sqlalchemy

print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

# sqlite 엔진(메모리 DB)
engine = create_engine('sqlite:///:memory:', echo=True)

# 메타데이터 생성(컬럼, 테이블 등)
metadata = MetaData()

# users 테이블 객체 생성
users = Table('users', metadata, Column('id', Integer, primary_key=True)
              , Column('name', String)
              , Column('fullname', String))

# addresses 테이블 객체 생성
addresses = Table('addresses', metadata
                  , Column('id', Integer, primary_key=True)
                  , Column('user_id', None, ForeignKey('users.id'))
                  , Column('email_address', String, nullable=False))

# sqlite DB에 테이블 생성
metadata.create_all(engine)

#insert 예제 (to users 테이블)
ins = users.insert()
print(str(ins))
ins = users.insert().values(id=1, name='Jack', fullname='Jack Jones')
print(str(ins))
ins.compile().params

# db에 연결
conn = engine.connect()
print(conn)
# 자료 인서트
result = conn.execute(ins)
# 인서트 결과
print("insert count:", result.inserted_primary_key)

#또 다른 방법
ins = users.insert()
conn.execute(ins, id=2, name='Wendy', fullname='Wendy William')
# 인서트 결과
print("insert count:", result.inserted_primary_key)

#여러 줄 인서트
conn.execute(addresses.insert(),
             [{'user_id':1, 'email_address':'jack@yahoo.com'}
            ,{'user_id':1, 'email_address':'jack@gmail.com'}
            ,{'user_id':2, 'email_address':'wendy@yahoo.com'}
            ,{'user_id':2, 'email_address':'wendy@gmail.com'}])
# 인서트 결과
print("insert count:", result.inserted_primary_key)

#select 연습
from sqlalchemy import select

s = select([users])
rslt = conn.execute(s)
for row in rslt:
    print(row)

print()

s = select([addresses])
rslt = conn.execute(s)

for row in rslt:
    print(row)

s = select([users])
rslt = conn.execute(s)
row = rslt.fetchone()
print('Access dictionary')
print('name:', row['name'], ', full name:', row['fullname'])
print()
print('Access index')
print('name:', row[1], ', full name:', row[2])
print()
print('Using Column Object')

s = select([addresses])
rslt = conn.execute(s)
for row in rslt:
    print('id:', row[addresses.c.id], ',user_id:', row[addresses.c.user_id], ', email_addres:', row[addresses.c.email_address])

print('추출하고자 하는 필드만 출력')
s = select([addresses.c.user_id, addresses.c.email_address])
rslt = conn.execute(s)
for row in rslt:
    print('user_id:', row[addresses.c.user_id], ', email_addres:', row[addresses.c.email_address])

print()
print('두개 테이블 추출')
s = select([users, addresses])
rslt = conn.execute(s)
for row in rslt:
    print(row)

print()
print('Where조건')
s = select([users, addresses]).where(users.c.id == addresses.c.id)
rslt = conn.execute(s)
for row in rslt:
    print(row)


print("Conjunction")
rslt.close()

