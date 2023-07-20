from pydantic import BaseModel


class LoggerConstructor(BaseModel):
    title: str = ""
    description: str = ""
    level: str = "default"
    error: str = None
