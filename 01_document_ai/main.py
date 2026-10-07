from pathlib import Path
import json
import time

from src.vision import analizar_imagen


INPUT_DIR = Path("documentos/entrada")
OUTPUT_DIR = Path("resultados")
MODEL = "qwen2.5vl:7b"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    imagenes = [
        archivo
        for archivo in INPUT_DIR.iterdir()
        if archivo.suffix.lower() in {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
        }
    ]

    if not imagenes:
        print("No hay imágenes en documentos/entrada/")
        return

    for imagen in imagenes:

        print("=" * 70)
        print(f"Procesando: {imagen.name}")
        print("=" * 70)

        try:
            # ---------------------------------------------------------
            # INICIO DEL CRONÓMETRO
            # ---------------------------------------------------------
            inicio = time.perf_counter()

            # ---------------------------------------------------------
            # ANÁLISIS DEL DOCUMENTO
            # ---------------------------------------------------------
            resultado = analizar_imagen(imagen)

            # ---------------------------------------------------------
            # FIN DEL CRONÓMETRO
            # ---------------------------------------------------------
            fin = time.perf_counter()

            tiempo_procesamiento = fin - inicio

            # ---------------------------------------------------------
            # METADATA DEL PROCESAMIENTO
            # ---------------------------------------------------------
            resultado["metadata"] = {
                "archivo": imagen.name,
                "modelo": MODEL,
                "tiempo_procesamiento_segundos": round(
                    tiempo_procesamiento, 2
                ),
                "tiempo_procesamiento_formateado": (
                    f"{tiempo_procesamiento:.2f} segundos"
                ),
            }

            # ---------------------------------------------------------
            # MOSTRAR RESULTADO
            # ---------------------------------------------------------
            print("\nJSON EXTRAÍDO:\n")

            print(
                json.dumps(
                    resultado,
                    ensure_ascii=False,
                    indent=4,
                )
            )

            # ---------------------------------------------------------
            # GUARDAR RESULTADO
            # ---------------------------------------------------------
            nombre_salida = OUTPUT_DIR / f"{imagen.stem}.json"

            nombre_salida.write_text(
                json.dumps(
                    resultado,
                    ensure_ascii=False,
                    indent=4,
                ),
                encoding="utf-8",
            )

            print(
                f"\nTiempo de procesamiento: "
                f"{tiempo_procesamiento:.2f} segundos"
            )

            print(
                f"Resultado guardado en: {nombre_salida}"
            )

        except Exception as error:
            print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()