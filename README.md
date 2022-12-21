# web3_storage_manager boilerplate

## Develop

You need [pyenv](https://github.com/pyenv/pyenv) and [poetry](https://python-poetry.org/) available in development environment.

1. Setup Python version specified in `.python-version`

```console
pyenv install
```

2. Prepare virtual environment with required dependencies and activate it

```console
poetry install
poetry shell
```

3. Setup pre-commit git hooks to automate code quality check

```console
poetry run pre-commit install
```

4. Create `.env` and specify arguments

```console
cp .env.example
```

5. Run migrations

```console
alembic upgrade head
```

6. Run app

On a localhost

```console
python -m web3_storage_manager
```

Or in a container

```console
docker compose up
```

## Deploy

### With Docker CLI

1. Load environment variables

```console
export $(cat .env | xargs)
```

2. Deploy stack to Docker Swarm cluster

```console
docker stack deploy -c docker-compose.yml -c docker-compose.prod.yml <stack_name>
```

### With Ansible

```console
ANSIBLE_CONFIG=/path/to/ansible.cfg ansible-playbook -i /path/to/hosts.yml deploy.yml
```
