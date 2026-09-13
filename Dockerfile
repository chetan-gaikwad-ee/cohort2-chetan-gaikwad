FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Runtime config defaults — these map to app/config.py Settings.
# Override any of them at run time with `docker run -e KEY=value`.
ENV APP_VERSION=0.1.2 \
    ENVIRONMENT=production \
    LOG_LEVEL=INFO \
    PORT=8000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the app code
COPY . .

# --- Run as non-root ---
RUN useradd --create-home --uid 1000 appuser \
    && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]