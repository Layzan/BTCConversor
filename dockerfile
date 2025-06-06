# Usar uma imagem base minimalista e segura
FROM python:3.11-slim

# Evitar prompts interativos e garantir compatibilidade
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Criar e usar um usuário não-root (boa prática de segurança)
RUN adduser --disabled-password appuser
WORKDIR /app

# Copiar apenas o requirements antes para aproveitar o cache do Docker
COPY requirements.txt .

# Atualizar o sistema e instalar dependências necessárias para build de pacotes Python
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y build-essential gcc \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar o código da aplicação
COPY ./app ./app

# Ajustar permissões e trocar para o usuário não-root
RUN chown -R appuser:appuser /app
USER appuser

# Expor a porta da aplicação
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
