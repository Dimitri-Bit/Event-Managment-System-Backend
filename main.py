from fastapi import FastAPI
from routes import user_routes,role_routes,permission_routes,user_roles_routes,roles_permission_routes
from core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(role_routes.router)
app.include_router(user_routes.router)
app.include_router(permission_routes.router)
app.include_router(user_roles_routes.router)
app.include_router(roles_permission_routes.router)


