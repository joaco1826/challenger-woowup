# Utilizar la imagen oficial de Python 3.11 como base
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos para instalar las dependencias
COPY requirements.txt .

# Instalar las dependencias desde el requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto en el que FastAPI correrá
EXPOSE 8000

# Comando para ejecutar FastAPI usando Uvicorn
CMD ["uvicorn", "app.config.http.app:app", "--host", "0.0.0.0", "--port", "8000"]
