FROM python:latest

ENV IN_DOCKER=true


WORKDIR /finance-fastapi-sqlmodel

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["sh", "-c", "cd scripts && ./run-fastapi.sh"]
