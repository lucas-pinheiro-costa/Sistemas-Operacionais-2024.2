# Usar uma imagem base do Python
FROM python:3-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o script Python para o contêiner
COPY cliente-http.py .

# Executar o script Python
CMD ["python", "cliente-http.py"]
