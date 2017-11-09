#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/21 17:15
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 流行的ORM框架。

class SQLAlchemyTest(object):
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class Book(Base):
        from sqlalchemy import Column, String, Integer, Float

        __tablename__ = "book"
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(127))
        author = Column(String(63))
        price = Column(Float(7))
        state = Column(String(31))

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    Engine = create_engine("mysql://username:password@host:port/database", echo=True)
    # Base.metadata.create_all(Engine)

    Session = sessionmaker(bind=Engine)

    def test(self):
        session = SQLAlchemyTest.Session()
        sanguo = SQLAlchemyTest.Book(name="SanGuo", author="LuoGuanzhong", price=99.99, state="SellOut")
        honglou = SQLAlchemyTest.Book(name="HongLou", author="CaoXueqin", price=88.88, state="SellOut")
        shuihu = SQLAlchemyTest.Book(name="ShuiHu", author="ShiNaian", price=77.77, state="SellOut")
        xiyou = SQLAlchemyTest.Book(name="XiYou", author="WuChengen", price=66.66, state="SellOut")

        htp = SQLAlchemyTest.Book(name="DeepinGo", author="XiuCai")

        session.add(htp)
        session.add_all([sanguo, honglou, shuihu, xiyou])
        session.commit()

        books = session.query(SQLAlchemyTest.Book).filter_by(name="SanGuo")
        for book in books:
            print(book.author)
