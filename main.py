from fastapi import FastAPI
from app.api import health, pets

app = FastAPI(
    title="Vet Clinic API",
    version="1.0.0"
)

# register routers
app.include_router(health.router)
app.include_router(pets.router)
