from fastapi import FastAPI
import uvicorn
import time
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import authRoutes
from routes.user import userRoutes
from routes.genres import genresRoutes

app = FastAPI()

app.include_router(authRoutes)
app.include_router(userRoutes)
app.include_router(genresRoutes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app) # localhost:8000


time.sleep(10)

# CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# # création des tables
# Base.metadata.create_all(bind=engine)

# # Créer un admin par défaut si aucun n'existe
# def create_admin():
#     db = SessionLocal()
#     admin_username = "admin"
#     admin_password = "11"

#     admin_exist = db.query(Utilisateur).filter_by(username=admin_username).first()
#     if not admin_exist:
#         hashed_password = generate_password_hash(admin_password)
#         admin_user = Utilisateur(username=admin_username, password_hash=hashed_password)
#         db.add(admin_user)
#         db.commit()
#         print("Admin créé avec succès")
    
#     db.close()

# create_admin()
