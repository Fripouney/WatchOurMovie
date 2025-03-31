FROM python:3.11

WORKDIR /app

COPY . .

# Installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Port FastAPI
EXPOSE 8000

# Lance l'app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
