from fastapi import APIRouter, Depends, BackgroundTasks

from src.application.trello.sync_trello_state import SyncTrelloStateOperacionOperacion
from src.interfaces.dto.trello_webhook_dto import TrelloWebhookPayload
from src.interfaces.dependencias.trello import dp_card_id

router = APIRouter(prefix="/trello", tags=["Webhooks"])


@router.head("/webhook")
async def validate_webhook_head():
    """
    Trello usa este endpoint (HEAD) para validar la URL al crear el webhook.
    """
    return {"status": "OK"}


@router.get("/webhook")
async def validate_webhook_get():
    """
    Algunas implementaciones de Trello pueden usar GET para la validación.
    """
    return {"status": "OK"}


@router.post("/webhook", status_code=200)
async def handle_webhook(
    payload: TrelloWebhookPayload,
    background_tasks: BackgroundTasks,
    use_case: SyncTrelloStateOperacionOperacion = Depends(dp_card_id),
):
    """
    Recibe el evento de Trello y lo procesa en segundo plano.
    """
    background_tasks.add_task(use_case.execute, payload)
    return {"message": "Webhook received and processing initiated."}
