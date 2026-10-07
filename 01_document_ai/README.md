
# Document AI Local con Modelos Multimodales

## Descripción

Este proyecto está enfocado en la experimentación con **Inteligencia Artificial aplicada al procesamiento automático de documentos**, utilizando modelos multimodales ejecutados localmente.

El objetivo principal es investigar cómo un modelo de lenguaje con capacidades de visión puede **comprender documentos visuales, interpretar su contenido y extraer información estructurada**, sin depender inicialmente de servicios externos de inteligencia artificial.

Actualmente, el proyecto utiliza **Qwen2.5-VL 7B** mediante **Ollama** para analizar imágenes de documentos.

---

## Objetivo

El objetivo es desarrollar progresivamente un sistema local de **Document AI** capaz de transformar documentos no estructurados, como:

* documentos escaneados;
* formularios;
* fichas;
* informes;
* certificados;
* documentos académicos;
* tablas;
* imágenes de documentos;
* archivos PDF;

en información que pueda ser utilizada posteriormente por aplicaciones o procesos automáticos.

La idea central es pasar de:

```text
Documento visual
        ↓
Información difícil de procesar automáticamente
```

a:

```text
Documento visual
        ↓
Modelo multimodal
        ↓
Comprensión del documento
        ↓
Extracción de información
        ↓
Datos estructurados
```

---

## ¿En qué se enfoca actualmente?

La primera etapa del proyecto está enfocada en comprobar la capacidad de un **modelo multimodal local para comprender documentos reales**.

No se busca únicamente realizar OCR.

El objetivo es que el modelo pueda **interpretar el documento completo**, entendiendo la relación entre:

* textos;
* campos;
* valores;
* títulos;
* secciones;
* tablas;
* fechas;
* nombres;
* códigos;
* instrucciones;
* información contextual.

Por ejemplo, ante una ficha académica, el modelo debe ser capaz de identificar que un determinado texto corresponde al título, que otro corresponde al docente, que existe una sección de evaluación y que una tabla contiene diferentes campos relacionados.

Por lo tanto, el proyecto se enfoca en **comprensión y extracción documental mediante modelos multimodales**, y no solamente en reconocimiento óptico de caracteres.

---

## ¿Qué hace actualmente?

Actualmente se puede proporcionar una **imagen de un documento** al sistema.

El sistema utiliza:

```text
Python
   ↓
Ollama
   ↓
Qwen2.5-VL 7B
   ↓
Análisis visual del documento
   ↓
Extracción de información
```

El modelo analiza la imagen y puede identificar información como:

* texto completo o parcial;
* nombres;
* fechas;
* códigos;
* títulos;
* campos;
* valores;
* secciones;
* tablas;
* contenido de diferentes apartados;
* información adicional presente en el documento.

Además, se le indica explícitamente que **no invente información** y que identifique como no disponible aquella información que no pueda leer correctamente.

---

## Primera prueba

Como prueba inicial se utilizó una ficha académica escaneada.

El modelo fue capaz de interpretar información relacionada con:

* institución;
* actividad;
* título;
* unidad didáctica;
* programa;
* turno;
* docente;
* contenidos;
* metodología;
* evaluación;
* fecha;
* firmas;
* información presente en tablas.

Esto permitió comprobar que **Qwen2.5-VL puede utilizarse localmente para realizar tareas de comprensión y extracción de información documental**.

---

## ¿Por qué utilizar un modelo multimodal?

Los documentos reales no están compuestos únicamente por texto.

La información puede estar organizada visualmente mediante:

* tablas;
* columnas;
* encabezados;
* formularios;
* secciones;
* cuadros;
* posiciones relativas;
* diferentes tipos de contenido.

Un modelo multimodal permite analizar simultáneamente el **contenido visual y textual** del documento.

Por esta razón, el proyecto busca evaluar qué tan lejos se puede llegar utilizando un modelo de visión y lenguaje ejecutado localmente.

---

## Enfoque del proyecto

El proyecto sigue un enfoque experimental.

Se busca evaluar diferentes aspectos de la extracción documental:

### 1. Comprensión visual

Determinar si el modelo puede interpretar correctamente documentos escaneados o fotografiados.

### 2. Extracción de información

Obtener los datos relevantes presentes en el documento.

### 3. Comprensión de estructura

Identificar campos, secciones y tablas, manteniendo la relación entre los elementos.

### 4. Estructuración

Transformar posteriormente la respuesta del modelo en formatos estructurados, principalmente **JSON**.

### 5. Automatización

Evolucionar desde el procesamiento de una imagen individual hacia el procesamiento automático de documentos completos y lotes de documentos.

---

## Próximo objetivo: extracción estructurada

Actualmente el modelo ya puede interpretar el documento y devolver la información encontrada.

El siguiente paso es hacer que esa información pueda ser utilizada directamente por software.

Por ejemplo:

```text
Documento
    ↓
Qwen2.5-VL
    ↓
Comprensión
    ↓
Extracción
    ↓
JSON
```

En lugar de obtener únicamente texto libre:

```text
El docente es...
La institución es...
La fecha es...
```

se busca obtener:

```json
{
    "tipo_documento": "...",
    "institucion": "...",
    "titulo": "...",
    "docente": "...",
    "fecha": "...",
    "contenido": {},
    "metodologia": [],
    "evaluacion": []
}
```

Esto permitiría que la información extraída pueda ser utilizada posteriormente por:

* aplicaciones;
* APIs;
* bases de datos;
* procesos ETL;
* sistemas de búsqueda;
* sistemas de clasificación;
* procesos de automatización.

---

## Evolución esperada

El proyecto busca evolucionar progresivamente desde una prueba de concepto hacia un pipeline completo de Document AI.

### Etapa actual

```text
Imagen
   ↓
Qwen2.5-VL
   ↓
Comprensión del documento
   ↓
Extracción de información
```

### Siguiente etapa

```text
Imagen
   ↓
Qwen2.5-VL
   ↓
Extracción estructurada
   ↓
JSON validado
```

### Etapa posterior

```text
PDF
   ↓
Procesamiento de páginas
   ↓
Qwen2.5-VL
   ↓
Información por página
   ↓
Consolidación
   ↓
Documento estructurado
```

### Objetivo a futuro

```text
PDF / Imagen
      ↓
Preprocesamiento
      ↓
Clasificación del documento
      ↓
Comprensión multimodal
      ↓
Extracción
      ↓
Validación
      ↓
JSON / Base de datos
      ↓
Aplicaciones y automatizaciones
```

---

## Alcance actual

Actualmente el proyecto se encuentra en una **fase de experimentación y prueba de concepto**.

El foco inmediato es evaluar la capacidad de modelos multimodales locales para resolver tareas de **comprensión y extracción de información desde documentos reales**.

La prioridad no es únicamente obtener texto, sino estudiar si un modelo local puede comprender la estructura y el significado del documento y convertir esa información en datos aprovechables por otros sistemas.

---

## Visión

La visión del proyecto es construir una solución de **Document AI ejecutada localmente**, donde documentos no estructurados puedan convertirse automáticamente en información estructurada y utilizable.

En términos simples:

> **Dar un documento al modelo y obtener de forma automática los datos que contiene, respetando su estructura y contexto.**

El proyecto parte de esta capacidad básica y busca evolucionar progresivamente hacia un sistema completo de procesamiento documental con modelos multimodales locales.
