from sqlalchemy import TIMESTAMP, Column, Integer, String, func
from sqlalchemy.orm import relationship

from web3_storage_manager.db.base_class import Base
from web3_storage_manager.db.models.crust_order import CrustOrder  # noqa


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    cid = Column(String)
    filesize = Column(Integer)

    crust_orders = relationship("CrustOrder", back_populates="content")

    status = Column(String, index=True, nullable=True)

    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
