from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import backref, relationship

from web3_storage_manager.db.base_class import Base
from web3_storage_manager.db.models.crust_order import CrustOrder

class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    cid = Column(String)
    filesize = Column(Integer)

    owner = relationship("User", back_populates="content")
    owner_id = Column(Integer, ForeignKey("users.id"))
    crust_orders = relationship("CrustOrder", back_populates="content")


    status = Column(String, index=True, nullable=True)

    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
