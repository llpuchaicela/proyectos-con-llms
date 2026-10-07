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
Analiza cuidadosamente el documento de esta imagen.

Este sistema es un extractor documental GENERICO.
El documento puede ser de cualquier tipo.

Puede tratarse, por ejemplo, de:

- una ficha académica;
- una factura;
- un certificado;
- un formulario;
- un contrato;
- un informe;
- una solicitud;
- un documento de identidad;
- un comprobante;
- una tabla;
- una carta;
- un documento administrativo;
- un documento escaneado;
- una fotografía de un documento;
- o cualquier otro tipo de documento.

NO asumas un tipo de documento específico.

Tu tarea es comprender el documento y extraer TODA la información
visible y relevante.

Devuelve ÚNICAMENTE un objeto JSON válido.
No escribas explicaciones.
No escribas texto antes ni después del JSON.
No utilices bloques Markdown como ```json.

Utiliza esta estructura general:

{
    "tipo_documento": null,
    "descripcion": null,
    "campos": {},
    "secciones": [],
    "tablas": [],
    "texto_completo": null,
    "elementos_adicionales": []
}

REGLAS:

1. Identifica primero qué tipo de documento es.

2. Describe brevemente el propósito o contenido general
   del documento.

3. En "campos", identifica los datos relevantes encontrados.
   Los nombres de los campos deben ser creados dinámicamente
   según el documento.

   Ejemplo:

   "campos": {
       "nombre": "...",
       "fecha": "...",
       "numero_documento": "...",
       "institucion": "..."
   }

   NO utilices campos que no existan en el documento.

4. En "secciones", identifica las diferentes partes o apartados
   del documento.

   Ejemplo:

   "secciones": [
       {
           "nombre": "Datos personales",
           "contenido": "..."
       },
       {
           "nombre": "Observaciones",
           "contenido": "..."
       }
   ]

5. En "tablas", identifica todas las tablas visibles.

   Cada tabla debe conservar sus encabezados y filas.

   Ejemplo:

   "tablas": [
       {
           "nombre": "Detalle",
           "columnas": ["Producto", "Cantidad", "Precio"],
           "filas": [
               ["Producto A", "2", "10.00"],
               ["Producto B", "1", "15.00"]
           ]
       }
   ]

6. En "texto_completo", incluye el texto visible del documento
   en la medida en que pueda ser leído correctamente.

7. En "elementos_adicionales", incluye información relevante
   que no encaje en campos, secciones o tablas.

8. Conserva los valores exactamente como aparecen cuando sea
   posible.

9. No inventes información.

10. Si un dato existe pero no puede leerse correctamente,
    utiliza null.

11. Si una sección no existe, utiliza una lista vacía [].

12. Si no existen tablas, utiliza [].

13. Si no existen elementos adicionales, utiliza [].

14. No conviertas automáticamente información ambigua en una
    interpretación.

15. Mantén las relaciones entre los datos.

16. Si existen firmas, sellos, logotipos, encabezados,
    códigos, números, fechas u otros elementos relevantes,
    inclúyelos dentro de la estructura correspondiente.

17. Si el documento contiene información repetida,
    conserva la información de manera coherente.

18. El objetivo NO es resumir el documento.
    El objetivo es EXTRAER la información que contiene.

19. El resultado final debe ser JSON válido.
""",
                "images": [str(image_path)],
            }
        ],
    )

    contenido = response["message"]["content"].strip()

    # Eliminar posibles bloques Markdown
    if contenido.startswith("```"):
        contenido = contenido.replace("```json", "")
        contenido = contenido.replace("```", "")
        contenido = contenido.strip()

    try:
        resultado = json.loads(contenido)

    except json.JSONDecodeError as error:
        raise ValueError(
            "El modelo no devolvió un JSON válido.\n"
            f"Error: {error}\n\n"
            f"Respuesta recibida:\n{contenido}"
        )

    return resultado