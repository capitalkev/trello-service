from fastapi import Depends
from sqlalchemy.orm import Session

from src.application.trello.sync_trello_state import SyncTrelloStateOperacion
from src.infrastructure.postgresql.connection import get_db
from src.infrastructure.postgresql.repository.trello import PostgresOperacionRepository


def dp_card_id(db: Session = Depends(get_db)) -> SyncTrelloStateOperacion:
    repository = PostgresOperacionRepository(db)
    return SyncTrelloStateOperacion(repository)
