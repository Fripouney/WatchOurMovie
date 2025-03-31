FROM node:18

WORKDIR /app

# Déclaration de l'argument TMDB_TOKEN attendu depuis docker-compose
ARG TMDB_TOKEN

# Copier les fichiers nécessaires d'abord
COPY package.json package-lock.json ./

# Installer les dépendances
RUN npm install -g @angular/cli && npm install

# Copier le reste du projet
COPY . .

# Injecter dynamiquement le token dans le fichier Angular d'environnement
RUN sed -i "s|tmdbToken: ''|tmdbToken: '${TMDB_TOKEN}'|" ./src/environments/environment.ts

# Exposer le port 4200 pour ng serve
EXPOSE 4200

# Démarrer le serveur Angular
CMD ["ng", "serve", "--host", "0.0.0.0"]
