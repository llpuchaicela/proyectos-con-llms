from pathlib import Path
import json
import ollama


MODEL = "qwen2.5vl:7b"

def analizar_imagen(image_path: Path) -> dict:

    if not image_path.exists():
        raise FileNotFoundError(f"No existe: {image_path}")

    response = ollama.chat(
        model=MODEL,
        format="json",
        messages=[
            {
                "role": "user",
                "content": """
Analiza cuidadosamente el documento de esta imagen.

Eres un sistema GENERICO de Document AI.
El documento puede ser de cualquier tipo:
factura, certificado, formulario, contrato, informe,
carta, documento académico, documento administrativo,
comprobante, documento de identidad, tabla, documento
escaneado, fotografía u otro.

NO asumas un tipo específico de documento.

OBJETIVO:
Extraer toda la información visible y relevante.
NO resumir.
NO inventar información.

Devuelve únicamente JSON válido con esta estructura:

{
    "tipo_documento": null,
    "descripcion": null,
    "campos": {},
    "secciones": [],
    "tablas": [],
    "texto_completo": null,
    "elementos_adicionales": [],
    "evaluacion": {
        "calidad_global": 0,
        "completitud": 0,
        "estructura": 0,
        "legibilidad": 0,
        "confianza": 0
    }
}

REGLAS DE EXTRACCION:

- Identifica el tipo de documento.
- Extrae los datos relevantes en "campos".
- Crea dinámicamente los nombres de los campos.
- Identifica todas las secciones.
- Identifica todas las tablas y conserva encabezados y filas.
- Transcribe el texto visible en "texto_completo".
- Incluye firmas, sellos, códigos, fechas, números,
  encabezados y notas cuando sean relevantes.
- Conserva los valores tal como aparecen.
- No inventes información.
- Usa null cuando un dato exista pero sea ilegible.
- Usa [] cuando no existan secciones, tablas o elementos adicionales.
- Mantén las relaciones entre los datos.

EVALUACION:

Después de realizar la extracción, evalúa tu propio resultado
utilizando una escala de 0 a 100.

"calidad_global":
Calidad general de la extracción.

"completitud":
Cantidad de información relevante que fue recuperada.

"estructura":
Qué tan correctamente se identificaron campos, secciones y tablas.

"legibilidad":
Qué tan correctamente se leyó el contenido visible.

"confianza":
Nivel general de confianza en la extracción.

La evaluación debe basarse únicamente en la información visible
en la imagen.

No inventes información para mejorar la puntuación.

Devuelve únicamente el JSON.
""",
                "images": [str(image_path)],
            }
        ],
        options={
            "temperature": 0.0,
            "num_ctx": 8192,
            "num_predict": 3000,
        },
    )

    contenido = response["message"]["content"].strip()

    try:
        return json.loads(contenido)

    except json.JSONDecodeError as error:
        raise ValueError(
            "El modelo no devolvió un JSON válido.\n"
            f"Error: {error}\n\n"
            f"Respuesta recibida:\n{contenido}"
        )