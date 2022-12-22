import uvicorn
from multiprocess import Process

from web3_storage_manager.db.session import SessionLocal
from web3_storage_manager.services.web3_uploader import Web3Uploader
from web3_storage_manager.web import app


def make_deals() -> None:
    print("started")
    with SessionLocal() as db:
        web3_uploader = Web3Uploader()
        web3_uploader.check_not_uploaded_content(db)


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    api_process = Process(target=start_server)
    deals_process = Process(target=make_deals)
    api_process.start()
    deals_process.start()
    api_process.join()
