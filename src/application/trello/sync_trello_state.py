from src.domain.interfaz import IOperacionRepository
from src.interfaces.dto.trello_webhook_dto import TrelloWebhookPayload


class SyncTrelloStateOperacion:

    LIST_TO_STATE_MAP = {
        "6931c938b831579f3f32f018": "Adelantos",
        "69a6f5fd1947cdca98a2d12e": "Excedentes",
        "63c6bca9d01cf30221c531d7": "Verificaciones",
        "6932e02c1f283ca555a8de76": "Verificaciones + 2",
        "65eb2557db11a94991727330": "Revision",
        "63a0f8e25d19ca01f565866d": "Reparo",
        "6269521e30ad430a3b02c424": "Riesgos Peru",
        "5f2347df28ff96020053e1ad": "Aprobacion Chile",
        "615f48d79ba36711880ffd19": "Operaciones",
        "5eceb24cff10a13c36c457d2": "Curse",
        "5ecee3b412c156153a0b5a8e": "Tesoreria",
        "64948367102db216e87a055c": "Pendiente 2DO Desembolso",
        "670e562121c95a693093ce3b": "Cerrado",
        
    }

    def __init__(self, operacion_repo: IOperacionRepository):
        self.operacion_repo = operacion_repo

    def execute(self, payload: TrelloWebhookPayload) -> None:
        action = payload.action

        if action.type == "updateCard" and action.data.listAfter:

            trello_card_id = action.data.card.id
            nueva_lista_id = action.data.listAfter.id

            # Aquí usamos "OTRO" como valor por defecto si el ID no está en el mapa
            nuevo_estado_bd = self.LIST_TO_STATE_MAP.get(nueva_lista_id, "OTRO")

            print(f"Intento de actualización para la tarjeta: {trello_card_id} al estado {nuevo_estado_bd}")

            actualizacion_exitosa = self.operacion_repo.update_estado_by_card_id(
                card_id=trello_card_id, nuevo_estado=nuevo_estado_bd
            )

            if actualizacion_exitosa:
                print(f"ÉXITO: Tarjeta {trello_card_id} actualizada en la BD al estado {nuevo_estado_bd}.")
            else:
                print(f"INFO: Tarjeta {trello_card_id} no encontrada en la BD. Se ignora el evento.")
