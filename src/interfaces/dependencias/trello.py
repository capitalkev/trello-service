from fastapi import Depends
from sqlalchemy.orm import Session

from src.application.trello.sync_trello_state import SyncTrelloStateOperacionOperacion
from src.infrastructure.postgresql.connection import get_db
from src.infrastructure.postgresql.repository.trello import PostgresOperacionRepository


def dp_card_id(db: Session = Depends(get_db)) -> SyncTrelloStateOperacionOperacion:
    repository = PostgresOperacionRepository(db)
    return SyncTrelloStateOperacionOperacion(repository)
