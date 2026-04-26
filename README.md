# Gestión de Biblioteca Templaria para Google Drive

Este directorio sirve como base de operaciones para la recopilación, organización y eventual subida a Google Drive de material de investigación histórica sobre la Orden del Temple.

##  Estructura de Carpetas Sugerida (Para Drive)

A medida que descargues los PDFs desde los enlaces del archivo `index.md`, deberás organizarlos localmente (o directamente en tu Google Drive) manteniendo el siguiente árbol de directorios para asegurar un control de calidad óptimo:

```text
Biblioteca_Templaria_Drive/
 ├── 1_Historia_General/
 ├── 2_Origen_y_Fundacion/
 ├── 3_Caida_de_la_Orden/
 ├── 4_Mitos_y_Leyendas/
 ├── 5_Cruzadas/
 └── 6_Analisis_Academico/
```

## 🤖 Prompt Maestro para Continuar la Búsqueda

Si deseas ampliar esta biblioteca en el futuro utilizando un asistente de IA, copia y pega el siguiente prompt. Está calibrado para continuar la metodología legal y estructurada:

```text
Actúa como un asistente de investigación y automatización documental.

OBJETIVO:
Continuar la búsqueda de libros en PDF sobre los Caballeros Templarios desde fuentes legales (Project Gutenberg, Internet Archive, Open Library, dominio público). 

REGLAS:
- NO repitas los 20 libros de la Fase 1 (Addison, Lea, Mackey, Pike, etc.).
- Busca exclusivamente obras en ESPAÑOL, o traducciones académicas de textos latinos (ej. Cartas de Clemente V, Bulas Papales como Vox in excelso).
- Priorizar libros completos, tesis doctorales en repositorios universitarios de acceso abierto o documentos históricos.

PROCESO:
1. Busca 10 nuevos libros/documentos.
2. Clasifícalos según la estructura: Historia, Origen, Caída, Mitos, Cruzadas, Académico.
3. Entrégame el resultado en formato de tabla Markdown con:
   - Nombre sugerido del archivo: [Tema] - Autor - Título (Año).pdf
   - Título Original
   - Autor
   - Año
   - URL directa de la fuente
   - Breve sinopsis
```

## ☁️ Preparación para Subida a Drive

1. **Descarga Manual:** Entra a los links provistos en `index.md` y descarga el formato `.pdf` o `.epub`.
2. **Renombrado:** Renombra el archivo localmente utilizando la nomenclatura sugerida en la tabla.
3. **Clasificación:** Arrastra el archivo a su carpeta temática correspondiente.
4. **Subida:** Selecciona las 6 carpetas temáticas y arrástralas simultáneamente a tu cuenta de Google Drive.

*(Opcional)*: Para desarrolladores, se puede crear un script en Python utilizando la librería `PyDrive2` y `requests` que lea el archivo `index.md`, descargue los PDFs localmente y los suba por API a Google Drive.