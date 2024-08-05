from sqlmodel import SQLModel, Field

class CRUD(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    email: str
    # Add other fields and configurations as needed
