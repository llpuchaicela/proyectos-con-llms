from pathlib import Path
from src.vision import analizar_imagen


INPUT_DIR = Path("documentos/entrada")
OUTPUT_DIR = Path("resultados")


def main():
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    imagenes = [
        archivo
        for archivo in INPUT_DIR.iterdir()
        if archivo.suffix.lower() in {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp"
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
            resultado = analizar_imagen(imagen)

            print("\nRESULTADO:\n")
            print(resultado)

            nombre_salida = OUTPUT_DIR / f"{imagen.stem}.txt"

            nombre_salida.write_text(
                resultado,
                encoding="utf-8"
            )

            print(f"\nResultado guardado en: {nombre_salida}")

        except Exception as e:
            print(f"\nERROR procesando {imagen.name}:")
            print(e)


if __name__ == "__main__":
    main()