# Image officielle Python comme base
FROM python:3.9

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers dans l'image
COPY app.py /app/
COPY requirements.txt /app/

# Installation des dépendances
RUN pip install -r requirements.txt

# Port que l'application utilise
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]