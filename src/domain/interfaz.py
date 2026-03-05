from abc import ABC, abstractmethod


class IOperacionRepository(ABC):
    """
    Interfaz para el repositorio de operaciones. Define el contrato que cualquier
    implementación de repositorio debe seguir para interactuar con los datos de las operaciones.
    """

    @abstractmethod
    def update_estado_by_card_id(self, card_id: str, nuevo_estado: str) -> bool:
        """
        Actualiza el estado de una operación en la base de datos, buscando por el card_id de Trello.

        Args:
            card_id: El ID de la tarjeta de Trello a actualizar.
            nuevo_estado: El nuevo estado que se asignará a la operación.

        Returns:
            True si la actualización fue exitosa (se encontró y actualizó el registro),
            False en caso contrario (no se encontró ninguna operación con ese card_id).
        """
        pass
