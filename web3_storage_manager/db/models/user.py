from sqlalchemy import TIMESTAMP, Column, Integer, String, func
from sqlalchemy.orm import relationship

from web3_storage_manager.db.base_class import Base
from web3_storage_manager.db.models.content import Content

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    api_key = Column(String)
    content = relationship("Content", back_populates="owner")
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    )
