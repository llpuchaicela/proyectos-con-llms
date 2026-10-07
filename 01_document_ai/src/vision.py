from pathlib import Path
import ollama


MODEL = "qwen2.5vl:7b"


def analizar_imagen(image_path: Path) -> str:
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

Extrae toda la información visible.

Reglas:

1. Lee todo el texto que puedas identificar.
2. Identifica todos los campos y sus valores.
3. Extrae nombres, códigos, fechas, números y cualquier
   otro dato relevante.
4. Identifica tablas y extrae su contenido.
5. No inventes información.
6. Si un dato no es legible, utiliza null.
7. Conserva exactamente los valores encontrados.
8. No hagas un resumen: quiero los datos del documento.

Devuelve el resultado en español.
""",
                "images": [str(image_path)],
            }
        ],
    )

    return response["message"]["content"]