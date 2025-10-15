FROM python:3.12-slim

COPY src/requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --with-deps chromium

WORKDIR /src
COPY /src /src
CMD ["python", "main.py"]