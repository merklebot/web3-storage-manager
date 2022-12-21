from fastapi import APIRouter, Depends

from web3_storage_manager.db.models.content import Content
from web3_storage_manager.db.models.crust_order import CrustOrder
from web3_storage_manager.web.schemas.content import NewContent, ContentInDb

from web3_storage_manager.web import dependencies

from sqlalchemy.orm import Session

from web3_storage_manager.db.models.user import User
from web3_storage_manager.utils.crust import get_order_state

router = APIRouter()


@router.post('.add')
async def add_content(new_content: NewContent, user: User = Depends(dependencies.get_current_user),
                      db: Session = Depends(dependencies.get_db)):
    existing_content = db.query(Content).filter(Content.cid == new_content.cid, Content.owner_id == user.id).first()
    print(existing_content)
    if existing_content:
        return {
            'ok': False,
            'error': 'Content exists'
        }
    content = Content(cid=new_content.cid, filesize=new_content.filesize, owner_id=user.id)

    db.add(content)
    db.commit()
    return {
        'ok': True,
        'result': {
            'cid': content.cid,
            'filesize': content.filesize
        }
    }


@router.post('.listCrustOrders')
async def list_crust_orders(content_in: ContentInDb, user: User = Depends(dependencies.get_current_user),
                            db: Session = Depends(dependencies.get_db)):
    if content_in.id:
        content = db.query(Content).filter(Content.id == content_in.id, Content.owner_id == user.id).first()
    else:
        content = db.query(Content).filter(Content.id == content_in.cid, Content.owner_id == user.id).first()

    if not content:
        return {
            'ok': False,
            'error': 'Content not found'
        }

    crust_orders = db.query(CrustOrder).filter(CrustOrder.content_id == content.id).all()
    return {
        'ok': True,
        'result': crust_orders
    }


@router.post('.listCrustReplicas')
async def list_crust_replicas(content_in: ContentInDb, user: User = Depends(dependencies.get_current_user),
                              db: Session = Depends(dependencies.get_db)):
    if content_in.id:
        content = db.query(Content).filter(Content.id == content_in.id, Content.owner_id == user.id).first()
    else:
        content = db.query(Content).filter(Content.id == content_in.cid, Content.owner_id == user.id).first()

    if not content:
        return {
            'ok': False,
            'error': 'Content not found'
        }
    crust_info = get_order_state(content.cid)
    return {
        'ok': True,
        'result': crust_info['replicas']
    }