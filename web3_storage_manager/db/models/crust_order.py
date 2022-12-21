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

class CrustOrder(Base):
    __tablename__ = "crust_orders"

    id = Column(Integer, primary_key=True, index=True)

    content = relationship("Content", back_populates="crust_orders")
    content_id = Column(Integer, ForeignKey("content.id"))

    status = Column(String)
    error_info = Column(String, nullable=True)

    cid = Column(String)
    filesize = Column(Integer)

    extrinsic_hash = Column(String)
    block_number = Column(Integer)
    tips = Column(Integer)
    memo = Column(String)

    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
