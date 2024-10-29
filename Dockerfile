FROM python:3.11-slim



WORKDIR /usr/src/app

COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install  --no-root

CMD ["python", "app.py"]