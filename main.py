from fastapi import FastAPI
from routes import user_routes, parties_routes, auth_routes
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database.database import sessionmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    if sessionmanager._engine is not None:
        await sessionmanager.close()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router)
app.include_router(parties_routes.router)
app.include_router(auth_routes.router)
