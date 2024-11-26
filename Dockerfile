# IMG do Python
FROM python:3.12-slim

# Define o diretório
WORKDIR /notify

# Instala as depedências do SO
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o script wait-for-it.sh para o container
COPY wait-for-it.sh /notify/

# Atribui permissão de execução para o container
RUN chmod +x /notify/wait-for-it.sh

# Copia o arquivo requirements.txt com as depdências da aplicação.
COPY requirements.txt /notify/

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

# Copia o código da aplicação para o container
COPY . /notify/

# Definir variáveis de ambiente
ENV DJANGO_SETTINGS_MODULE=config.settings \
    PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Expor na porta 8000 do container
EXPOSE 8000

# Comando para rodar no servidor django
# CMD ["uwsgi", "--ini", "notify_uwsgi.ini"]