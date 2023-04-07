
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app

RUN python -m venv /opt/venv
ENV PATH="opt/venv/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install dotenv

ENV PYTHONUNBUFFERED 1

COPY . /app

# EXPOSE 8000
ENTRYPOINT ["streamlit"]

CMD ["run", "src/main.py", "--server.port", "80"]