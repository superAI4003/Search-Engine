from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LLMOutput(Base):
    __tablename__ = 'llm_output'

    id = Column(Integer, primary_key=True, autoincrement=True)
    llm_id = Column(String, nullable=False)
    query = Column(Text, nullable=False)
    prompt = Column(Text, nullable=False)
    search_result = Column(Text, nullable=False)
    llm_out = Column(Text, nullable=False)
    vote = Column(Boolean, default=False)