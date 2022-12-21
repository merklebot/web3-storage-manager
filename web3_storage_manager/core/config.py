from pydantic import BaseSettings, Field


class DBSettings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL")


class WalletSettings(BaseSettings):
    CRUST_SEED: str = Field(..., env="CRUST_SEED")
    CRUST_RPC_NODE: str = Field(default="wss://rpc.crust.network", env="CRUST_RPC_NODE")


class Settings(BaseSettings):
    DB: DBSettings = DBSettings()
    WALLET_SETTINGS: WalletSettings = WalletSettings()


settings = Settings()
