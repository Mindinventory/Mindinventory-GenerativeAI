from pydantic import BaseModel

class User_Input(BaseModel):
    query: str
