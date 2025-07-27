from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user
from app.core.config import settings


# create FastAPI instance with metadat
app = FastAPI(
    title=settings.PROJECT_NAME,
    version='1.0.0',
    description='FastAPI simple crud appication'
)

# cors middleware for api accessing from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins =['*'],  # dev only
    allow_credentials =True,
    allow_headers = ['*'],
    allow_methods = ['*'],
                   )

# include routers
app.include_router(user.router, prefix='/user', tags=['Users'])

# Root health check

@app.get('/', tags=['Health'])
def health_check():
    return {"status":"ok", "app":settings.PROJECT_NAME}