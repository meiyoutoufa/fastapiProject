import traceback
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

# MySQL数据库配置
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:mikezhu@120.78.171.211:3306/food"

# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 数据库模型基础类
class Base(SQLModel):
    class Config:
        arbitrary_types_allowed = True

# # 创建数据库连接和会话
# @contextmanager
# def get_tx_db():
#     session = Session(engine)
#     try:
#         yield session
#         session.commit()  # 提交事务
#     except Exception:
#         session.rollback()  # 发生异常时回滚事务
#         print(traceback.format_exc())
#         raise
#     finally:
#         session.close()


def get_db():
    with Session(engine) as session:
        yield session