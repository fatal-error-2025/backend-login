from pydantic import BaseModel, EmailStr

# ------------------- Users -------------------
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # para Pydantic v2

# ------------------- Tasks -------------------
class TaskCreate(BaseModel):
    title: str
    precipitation: float = 0.0
    temperature: float = 0.0
    wind: float = 0.0

class TaskResponse(BaseModel):
    id: int
    title: str
    precipitation: float
    temperature: float
    wind: float
    user_id: int

    class Config:
        from_attributes = True  # para Pydantic v2
