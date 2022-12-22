from typing import Any

from pydantic import BaseSettings, Field, PostgresDsn, validator


class WalletSettings(BaseSettings):
    CRUST_SEED: str = Field(..., env="CRUST_SEED")
    CRUST_RPC_NODE: str = Field(default="wss://rpc.crust.network", env="CRUST_RPC_NODE")


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    WALLET_SETTINGS: WalletSettings = WalletSettings()


settings = Settings()
