# Fast API do Zero

## Instalação

```script
# Install Poetry
pip install pipx
pipx install poetr

# pyenv
pyenv update
pyenv install 3.13:latest
pyenv global 3.13
pyenv local 3.13.1 

# Execute Poetry
poetry new fast_zero
poetry env use 3.13.1 
poetry install   

# Install depedency
poetry add "fastapi[standard]"

# Hello
# interativo
# read_root()
python -i fast_zero/app.py

# Habilita ambiente virtual do poetry (venv)
poetry shell

# Executar o fast api
fastapi dev fast_zero/app.py

# Ruff - linter
poetry add --group dev ruff
ruff check .
ruff check . --fix
ruff format .

# Pytest - test e coverage
poetry add --group dev pytest pytest-cov
pytest
pytest --cov=fast_zero -vv
coverage html

# Taskipy: cria um alias para comandos
poetry add --group dev taskipy
task run
```


Curso do Dunossauro: https://fastapidozero.dunossauro.com/
