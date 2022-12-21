from pydantic import BaseModel


class NewContent(BaseModel):
    cid: str
    filesize: int


class ContentInDb(BaseModel):
    id: int | None
    cid: str | None