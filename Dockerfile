FROM python:3.12-slim

WORKDIR /src

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps chromium

COPY src/ .
CMD ["python", "main.py"]