FROM python:3.11-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Crear carpeta para el código
WORKDIR /app

# Copiar archivos de código
COPY shared_code.c .
COPY run_benchmark.py .

# Instalar dependencias de Python
RUN pip install --no-cache-dir psutil numpy

# Compilar la librería compartida
RUN gcc -fPIC -shared -o shared_code.so shared_code.c   

# Crear punto de montaje para resultados compartidos
RUN mkdir -p /mnt/shared_results

# Comando por defecto: ejecutar benchmark
CMD ["python3", "run_benchmark.py"]
