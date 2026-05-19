# cohort2-chetan-gaikwad

A FastAPI application with a health check endpoint.

## Prerequisites

- Python 3
- pip

## Setup

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

The server starts at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Verify

```bash
curl http://127.0.0.1:8000/health
```

## Test

```bash
pytest
```

## Sample Response

### `GET /health`

```json
{
  "status": "ok",
  "timestamp": "2026-05-19T10:30:00.000000Z",
  "version": "0.1.0",
  "environment": "development"
}
```
