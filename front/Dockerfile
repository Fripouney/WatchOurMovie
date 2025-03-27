# Build l'app
FROM node:18 AS builder

WORKDIR /app

COPY . .

RUN npm install && npm run build

# Servir l'app avec Nginx
FROM nginx:alpine

# Copie les fichiers compilés dans le dossier de Nginx
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
