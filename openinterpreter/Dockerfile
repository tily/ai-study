FROM python:3.11

WORKDIR /work
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin

ADD pyproject.toml .
ADD poetry.lock .
RUN poetry install

ENTRYPOINT ["poetry", "run"]
