import time

from sqlalchemy.orm import Session
from sqlalchemy import func

from web3_storage_manager.db.models.content import Content
from web3_storage_manager.db.models.crust_order import CrustOrder
from web3_storage_manager.utils.crust import make_storage_order
import datetime


class Web3Uploader:
    def __init__(self):
        pass

    def check_not_uploaded_content(self, db: Session):
        while True:
            print("starting content watching")
            content_for_upload = db.query(Content).filter(~Content.crust_orders.any()).all()
            for content in content_for_upload:
                tips = 0
                _memo = ''

                is_success, extrinsic_hash, block_number = make_storage_order(cid=content.cid, filesize=content.filesize, tips=tips, _memo=_memo)
                if is_success:
                    crust_order = CrustOrder(
                        content=content,
                        cid=content.cid,
                        filesize=content.filesize,
                        extrinsic_hash=extrinsic_hash,
                        block_number=block_number,
                        status='created',
                        tips=tips,
                        memo=_memo
                    )
                    db.add(crust_order)
                    db.commit()

            crust_orders_without_status = db.query(CrustOrder).filter(CrustOrder.status=='created').all()
            for crust_order in crust_orders_without_status:
                pass
            time.sleep(120)