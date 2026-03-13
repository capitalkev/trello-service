from fastapi import FastAPI
from src.interfaces.router import health, trello

from src.config import API_KEYS
from src.interfaces.middleware.api_key_auth import ApiKeyMiddleware


def create_app() -> FastAPI:
    application = FastAPI(
        title="Trello Webhook Service",
        description="A service to handle Trello webhooks and process events.",
        version="1.0.0",
    )
    application.add_middleware(ApiKeyMiddleware, api_keys=API_KEYS)
    application.include_router(health.router)
    application.include_router(trello.router)
    return application


app = create_app()
