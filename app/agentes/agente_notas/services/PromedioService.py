import requests
from .config import get_promedio_url
import unicodedata

class PromedioService:

    def normalizar_texto(self, texto: str) -> str:
        if not texto:
            return ""

        texto = texto.lower().strip()
        texto = unicodedata.normalize("NFD", texto)
        texto = texto.encode("ascii", "ignore").decode("utf-8")
        return texto


    def obtener_promedio_estudiante(self, id_estudiante: str, nombre_programa: str | None = None):

        try:
            base_url = get_promedio_url().rstrip("/")
            url = f"{base_url}/{id_estudiante}"

            resp = requests.get(url=url, timeout=60)

            if resp.status_code != 200:
                return {
                    "error": True,
                    "message": "No se pudo obtener el promedio del estudiante."
                }

            data = resp.json()

            if not isinstance(data, list) or not data:
                return {
                    "error": True,
                    "message": "No se encontró información del estudiante."
                }

            if nombre_programa:

                nombre_programa_normalizado = self.normalizar_texto(nombre_programa)

                programa_filtrado = next(
                    (
                        p for p in data
                        if nombre_programa_normalizado in 
                        self.normalizar_texto(p.get("DESC_PROG", ""))
                    ),
                    None
                )

                if not programa_filtrado:
                    return {
                        "error": True,
                        "message": f"No se encontró el programa '{nombre_programa}'."
                    }

                return {
                    "error": False,
                    "programa": programa_filtrado.get("DESC_PROG"),
                    "codigo_programa": programa_filtrado.get("PROGRAMA"),
                    "estado": programa_filtrado.get("ESTADO"),
                    "promedio_acumulado": round(float(programa_filtrado.get("PROM_ESTU", 0)), 2)
                }

            resultado = []

            for p in data:
                resultado.append({
                    "programa": p.get("DESC_PROG"),
                    "codigo_programa": p.get("PROGRAMA"),
                    "estado": p.get("ESTADO"),
                    "promedio_acumulado": round(float(p.get("PROM_ESTU", 0)), 2)
                })

            return {
                "error": False,
                "total_programas": len(resultado),
                "programas": resultado
            }

        except requests.RequestException as e:
            return {
                "error": True,
                "message": f"Error interno: {e}"
            }