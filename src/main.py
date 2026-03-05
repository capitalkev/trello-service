from fastapi import FastAPI
from src.interfaces.router import trello


def create_app() -> FastAPI:
    app = FastAPI(
        title="Trello Webhook Service",
        description="A service to handle Trello webhooks and process events.",
        version="1.0.0",
    )
    app.include_router(trello.router)
    return app


app = create_app()
