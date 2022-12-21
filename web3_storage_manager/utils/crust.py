from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from web3_storage_manager.core.config import settings
from web3_storage_manager.db.models.crust_order import CrustOrder
substrate = SubstrateInterface(url=settings.WALLET_SETTINGS.CRUST_RPC_NODE)
keypair = Keypair.create_from_mnemonic(settings.WALLET_SETTINGS.CRUST_SEED)


def make_storage_order(cid: str, filesize: int, tips: int, _memo:str):
    call = substrate.compose_call(
        call_module='Market',
        call_function='place_storage_order',
        call_params={
            'cid': cid,
            'reported_file_size': filesize,
            'tips': tips,
            '_memo': _memo
        }
    )

    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    try:
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Extrinsic '{receipt.extrinsic_hash}' sent and included in block '{receipt.block_number}'")
        return receipt.is_success, receipt.extrinsic_hash, receipt.block_number

    except SubstrateRequestException as e:
        print("Failed to send: {}".format(e))

def get_order_state(cid: str):
    info = substrate.query(
        module='Market',
        storage_function='FilesV2',
        params=[cid]
    )
    return info