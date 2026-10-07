from pathlib import Path
import json
import ollama


MODEL = "qwen2.5vl:7b"


def analizar_imagen(image_path: Path) -> dict:
    if not image_path.exists():
        raise FileNotFoundError(f"No existe: {image_path}")

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": """
Analiza cuidadosamente esta imagen como un sistema
de extracción documental.

Extrae TODA la información visible del documento.

Devuelve ÚNICAMENTE un objeto JSON válido.
No escribas explicaciones.
No escribas texto antes ni después del JSON.
No utilices bloques Markdown como ```json.

Utiliza exactamente esta estructura:

{
    "tipo_documento": null,
    "institucion": null,
    "titulo": null,
    "actividad": null,
    "unidad_didactica": null,
    "programa": null,
    "turno": null,
    "docente": null,
    "fecha": null,
    "contenido": {
        "procedimental": null,
        "conceptual": null,
        "actitudinal": null
    },
    "metodologia": [],
    "evaluacion": [],
    "firmas": [],
    "texto_adicional": []
}

Reglas:

1. Lee todo el texto que puedas identificar.
2. Identifica todos los campos y sus valores.
3. Conserva exactamente los valores encontrados.
4. No inventes información.
5. Si un campo no aparece o no es legible, utiliza null.
6. Si existen tablas, conviértelas en listas de objetos.
7. En "metodologia" conserva toda la información de la tabla.
8. En "evaluacion" conserva toda la información de la tabla.
9. En "firmas" incluye los nombres o cargos visibles.
10. En "texto_adicional" incluye cualquier información importante
    que no encaje en los demás campos.
11. Mantén el contenido completo, no hagas un resumen.
12. El resultado debe ser JSON válido.
""",
                "images": [str(image_path)],
            }
        ],
    )

    contenido = response["message"]["content"].strip()

    # El modelo podría devolver accidentalmente ```json ... ```
    if contenido.startswith("```"):
        contenido = contenido.replace("```json", "")
        contenido = contenido.replace("```", "")
        contenido = contenido.strip()

    try:
        return json.loads(contenido)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"El modelo no devolvió un JSON válido.\n"
            f"Error: {error}\n\n"
            f"Respuesta recibida:\n{contenido}"
        )