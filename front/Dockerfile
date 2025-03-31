FROM node:18

WORKDIR /app

# Installer les dépendances
COPY package.json package-lock.json ./
RUN npm install -g @angular/cli
RUN npm install

# Copier le reste du code source de l'application
COPY . .

# Exposer le port 4200 pour le serveur Angular
EXPOSE 4200

# Lancer l'application
CMD ["ng", "serve", "--host", "0.0.0.0"]