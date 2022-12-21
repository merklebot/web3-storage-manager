#!/usr/bin/env bash

alembic upgrade head

python -m web3_storage_manager
