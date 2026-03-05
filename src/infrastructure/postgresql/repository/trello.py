from sqlalchemy import text
from sqlalchemy.orm import Session

from src.domain.interfaz import IOperacionRepository


class PostgresOperacionRepository(IOperacionRepository):
    def __init__(self, db: Session):
        self.db = db

    def update_estado_by_card_id(self, card_id: str, nuevo_estado: str) -> bool:
        """
        Actualiza el estado de una operación si el card_id existe en la base de datos.
        """
        sql = text(
            "UPDATE operaciones SET estado = :nuevo_estado WHERE card_id = :card_id"
        )

        result = self.db.execute(
            sql, {"nuevo_estado": nuevo_estado, "card_id": card_id}
        )
        self.db.commit()

        return result.rowcount > 0
