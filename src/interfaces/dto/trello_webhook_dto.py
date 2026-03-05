from pydantic import BaseModel
from typing import Optional


class ListInfo(BaseModel):
    id: str
    name: str


class CardInfo(BaseModel):
    id: str
    name: str


class ActionData(BaseModel):
    card: Optional[CardInfo] = None
    listBefore: Optional[ListInfo] = None
    listAfter: Optional[ListInfo] = None
    # Permite otros campos sin romper la validación
    model_config = {"extra": "allow"}


class TrelloAction(BaseModel):
    type: str
    data: ActionData


class TrelloWebhookPayload(BaseModel):
    action: TrelloAction
    # Trello envía mucha más metadata, la ignoramos si no nos sirve
    model_config = {"extra": "ignore"}
