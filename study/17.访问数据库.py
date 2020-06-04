print('-----------SQLite-----------')
# SQLite 是一种嵌入式数据库，体积很小，经常被集成在应用程序中，甚至IOS 和Android 的App 中都可以集成
# Python 内置了SQLite3,
import sqlite3

# 连接数据库，数据库文件为test.db
conn = sqlite3.connect('test.db')
# 创建Cursor
cursor = conn.cursor()
# 执行SQL 语句
# cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
# 继续执行SQL
# cursor.execute('insert into user(id, name) values(\'1\', \'Michael\')')
# rowcount 返回插入的行数
# print(cursor.rowcount)
# 执行查询语句
cursor.execute('select * from user where id=?', ('1', ))
# 获得查询结果
values = cursor.fetchall()
print(values)
# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 断开数据库连接
conn.close()


print('-----------MySql-----------')
# 首先安装MySql 驱动
# pip install mysql-connector

# 导入mysql 驱动
import mysql.connector

conn = mysql.connector.connect(host='test.db.uuuwin.com', port=4417, user='race_dba_s4417', password='s4417.race.uw', database='race_shop')
cursor = conn.cursor()

cursor.execute('select * from user where id=%s', (6, ))
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()


print('-----------SQLAlchemy-----------')
# SQLAlchemy 是Python 的ORM 框架，用来将表结构映射到对象
from sqlalchemy import Column, String, create_engine, Integer, DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 创建对象的基类
Base = declarative_base()


# 定义User 对象
class User(Base):
    # 表名
    __tablename__ = 'user'

    # 表结构
    id = Column(BigInteger(), primary_key=True)
    name = Column(String(100))
    phone = Column(String(20))
    age = Column(Integer())
    create_time = Column(DateTime())


# 初始化数据库连接，字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://race_dba_s4417:s4417.race.uw@test.db.uuuwin.com:4417/race_shop')
# 创建DBSession，可以看做是数据库连接
BDSession = sessionmaker(bind=engine)

# 有了ORM，新增就可以视为添加了一个User 对象
# 创建session 对象
session = BDSession()
# 创建新的User 对象
new_user = User(name='sqlalchemy', phone='123123123', age=20, create_time=datetime.now())
# 添加到session
session.add(new_user)
# 提交保存到数据库
session.commit()

# 创建Query 查询，filter 是where 条件，调用one() 返回唯一行，调用all() 则返回所有行
user = session.query(User).filter(User.id == 123124).one()
print(type(user), user.name)

# 关闭session
session.close()


# ORM 框架也可以提供两个对象之间的一对多、多对多等功能
class Author(Base):
    __tablename__ = 'author'

    id = Column(BigInteger(), primary_key=True)
    name = Column(String(100))
    # 一对多
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(BigInteger(), primary_key=True)
    name = Column(String(100))
    # ‘多’的一方的book 表是通过外键关联到user 的
    author_id = Column(BigInteger(), ForeignKey('Author.id'))

