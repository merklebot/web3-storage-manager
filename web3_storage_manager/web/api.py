from fastapi import APIRouter

from web3_storage_manager.web.endpoints import content, users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users")
api_router.include_router(content.router, prefix="/content")
