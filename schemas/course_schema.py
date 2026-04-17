from typing import Optional
from pydantic import BaseModel, ConfigDict

class CourseSchema(BaseModel):
    id: Optional[int] = None
    title: str 
    course_classes: int
    hours: int

    model_config = ConfigDict(from_attributes=True)
    
        