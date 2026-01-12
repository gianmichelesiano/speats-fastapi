# Speats FastAPI

API backend per Speats.

## Requisiti

- Python 3.11+
- Docker (opzionale)

## Installazione locale
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

## Docker
```bash
docker build -t speats-fastapi .
docker run -p 8001:8001 speats-fastapi
```

## Endpoints

- `GET /health` - Health check
- `GET /hello/{name}` - Saluto personalizzato
- `GET /docs` - Swagger UI

## API URL

- Produzione: https://api.speats.ch
