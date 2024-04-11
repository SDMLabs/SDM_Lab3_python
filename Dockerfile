FROM python:3.10-buster
WORKDIR /app

COPY ./requirements ./requirements

RUN python -m venv ./.venv
RUN . ./.venv/bin/activate
RUN pip install -r requirements/freeze_requirments

COPY ./build ./build
COPY ./spaceship ./spaceship

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8000"]