from src.domain.interfaz import IOperacionRepository
from src.interfaces.dto.trello_webhook_dto import TrelloWebhookPayload


class SyncTrelloStateOperacion:

    LIST_TO_STATE_MAP = {
        "69a6f5fd1947cdca98a2d12e": "excedentes",
        "63c6bca9d01cf30221c531d7": "verificaciones",
        "6931c938b831579f3f32f018": "verificadas",
    }

    def __init__(self, operacion_repo: IOperacionRepository):
        self.operacion_repo = operacion_repo

    def execute(self, payload: TrelloWebhookPayload) -> None:
        action = payload.action

        if action.type == "updateCard" and action.data.listAfter:

            trello_card_id = action.data.card.id
            nueva_lista_id = action.data.listAfter.id

            nuevo_estado_bd = self.LIST_TO_STATE_MAP.get(nueva_lista_id)

            if nuevo_estado_bd:
                print(
                    f"Intento de actualización para la tarjeta: {trello_card_id} al estado {nuevo_estado_bd}"
                )

                actualizacion_exitosa = self.operacion_repo.update_estado_by_card_id(
                    card_id=trello_card_id, nuevo_estado=nuevo_estado_bd
                )

                if actualizacion_exitosa:
                    print(
                        f"ÉXITO: Tarjeta {trello_card_id} actualizada en la BD al estado {nuevo_estado_bd}."
                    )
                else:
                    print(
                        f"INFO: Tarjeta {trello_card_id} no encontrada en la BD. Se ignora el evento."
                    )
            else:
                print(
                    f"OMITIDO: La lista de Trello {nueva_lista_id} no está mapeada a ningún estado."
                )
