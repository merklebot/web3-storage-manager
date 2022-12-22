# Import all the models, so that Base has them before being
# imported by Alembic

from web3_storage_manager.db.base_class import Base  # noqa

from .models.content import *  # noqa
from .models.crust_order import *  # noqa
