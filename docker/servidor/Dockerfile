# Usar uma imagem base do Python
FROM python:3-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o script Python para o contêiner
COPY servidor-http.py .

# Expor a porta 8000
EXPOSE 8000

# Executar o script Python
CMD ["python", "servidor-http.py"]
