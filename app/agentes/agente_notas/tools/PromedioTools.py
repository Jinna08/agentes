from langchain.tools import tool
from ..services.PromedioService import PromedioService
from .context import get_id_estudiante

promedio_service = PromedioService()


@tool
def promedio_estudiante(nombre_programa: str = None):
    """
    Devuelve el promedio acumulado del estudiante.
    
    - Si no se especifica programa → lista todos los programas.
    - Si se especifica programa → devuelve solo ese programa.
    """

    id_estudiante = get_id_estudiante()

    if not id_estudiante:
        return {
            "error": True,
            "message": "No se identificó al estudiante"
        }

    return promedio_service.obtener_promedio_estudiante(
        id_estudiante=id_estudiante,
        nombre_programa=nombre_programa
    )
