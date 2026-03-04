from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DAG(Base):
    __tablename__ = "dags"
    id = Column(Integer, primary_key=True)
    dag_id = Column(String, unique=True)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    dag_id = Column(Integer, ForeignKey("dags.id"))
    task_id = Column(String)
    status = Column(String)
    retries = Column(Integer)
    max_retries = Column(Integer)
