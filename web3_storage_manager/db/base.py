# Import all the models, so that Base has them before being
# imported by Alembic

from web3_storage_manager.db.base_class import Base

from .models.user import *
from .models.content import *
from .models.crust_order import *