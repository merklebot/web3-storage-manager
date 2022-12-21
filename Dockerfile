FROM python:3.10.6 as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10.6
WORKDIR /web3_storage_manager
COPY --from=requirements-stage /tmp/requirements.txt /web3_storage_manager/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /web3_storage_manager/requirements.txt
COPY web3_storage_manager /web3_storage_manager/web3_storage_manager
COPY ./alembic.ini /web3_storage_manager/alembic.ini
COPY ./start.sh /web3_storage_manager/start.sh

ENTRYPOINT ["/bin/bash" ,"start.sh"]
