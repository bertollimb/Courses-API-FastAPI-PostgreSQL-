from core.database import Base
from sqlalchemy import Column, Integer, String

class CourseModel(Base):
    __tablename__ = 'courses'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(100))
    course_classes: int = Column(Integer)
    hours: int = Column(Integer)
    