# WatchOurMovie

## Architecture du projet

Notre projet est constitué d'une architecture classique pour un site web : une partie **frontend**, une partie **backend**, une **base de données** ainsi qu'une **API externe** pour récupérer des informations sur les films.

## Choix des technologies

Pour réaliser ce projet, nous avons eu recours à plusieurs technologies différentes :
- Pour le front, **Angular**, framework **JavaScript** simplifiant l'envoi de requêtes vers le back et organisant les pages web en composants.
- Pour le back, **FastAPI**, un framework **python** simple d'utilisation pour créer des API.
- Nous avons utilisé une base de données relationnelle **PostgreSQL**, suffisante pour les besoins du projet
- L'API pour récupérer les informations sur les films est **The Movie Database**, car il s'agit d'une API gratuite dont le rate limit n'est pas handicapant pour le projet.
- Le front, le back et la base de données sont chacun dans leur conteneur **Docker**, et le tout est orchestré par **Docker Compose**

## Fonctionnalités implémentées


