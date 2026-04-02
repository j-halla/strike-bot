FROM python:3.12-slim AS base
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS production
COPY . .
CMD ["python", "-m", "bot.main"]

FROM base AS development
RUN pip install watchfiles
CMD ["watchfiles", "python -m bot.main"]
