# WatchOurMovie

## Architecture du projet

Notre projet utilise une architecture assez classique : une partie **frontend**, une partie **backend**, une **base de données** ainsi qu'une **API externe** pour récupérer des informations sur les films.

## Choix des technologies

- Pour le front, **Angular**, framework **JavaScript** simplifiant l'envoi de requêtes vers le back et organisant les pages web en composants.
- Pour le back, **FastAPI**, un framework **python** simple d'utilisation pour créer des APIs.
- Nous avons utilisé une base de données relationnelle **PostgreSQL**, suffisante pour les besoins du projet.
- L'API pour récupérer les informations sur les films est **The Movie Database**, il s'agit d'une API gratuite dont le rate limit n'est pas handicapant pour le projet.
- Le front, le back et la base de données sont chacun dans leur conteneur **Docker**, et le tout est orchestré par **Docker Compose**

### Précisions techniques additionnelles

L'authentification est gérée avec des **tokens JWT**, c'est une méthode sécurisée et simple d'implémentation. Concernant la sécurité du token TMDB, il est stocké dans un fichier .env *(non founit dans le projet !!)* puis chargé **dynamiquement dans le docker compose**, qui lui même le charge dans l'environnement Angular lors du build du conteneur frontend.

Le projet a une **forte modularité**, surtout dans le backend, et possède de nombreux standards de développement Python et Angular (pas de main.py long de 3000 lignes cela vous est épargné).

## Fonctionnalités implémentées

Un utilisateur peut :
- Se connecter
- Ajouter ses amis
- Consulter le catalogue de films
- Obtenir des suggestions en fonction des films déjà vu par son groupe de visionnage (l'utilisateur sélectionne avec qui il souhaite voir un film à l'instant T)

### Perspectives

Un role administrateur pour les utilisateurs existe sur le site, sans fonctionnalité propre à ce rôle pour le moment, mais cela permet une meilleure maintenabilité à long terme pour toutes sortes de commandes d'administration.

Sur le catalogue de films, un système de pagination est à ajouter pour pouvoir consulter tous les films du catalogue. D'autres filtres pourraient aussi être ajoutés
