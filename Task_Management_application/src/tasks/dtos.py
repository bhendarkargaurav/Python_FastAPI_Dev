from pydantic import BaseModel
class TaskSchema(BaseModel):
    title: str
    desciption:str
    is_completed: bool = False