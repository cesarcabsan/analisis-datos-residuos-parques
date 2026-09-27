# Análisis de datos para concientización ambiental en parques

## 📌 Introducción
Este proyecto forma parte de mi servicio social en **CEFODEH** y busca fortalecer la conciencia ambiental en parques comunitarios y vecinales de Monterrey.  
La iniciativa se centra en el análisis de datos de residuos para identificar patrones de consumo y desecho, y difundir información clara y accesible a la comunidad.

## 🌍 Objetivos de Desarrollo Sostenible (ODS)
El proyecto se vincula con los siguientes ODS:
- **ODS 11: Ciudades y comunidades sostenibles** → Promover hábitos responsables de reciclaje y manejo de residuos en espacios públicos.  
- **ODS 12: Producción y consumo responsables** → Reducir plásticos de un solo uso y fomentar prácticas de separación adecuada de residuos.

## ⚙️ Arquitectura del Pipeline ETL
El pipeline implementado en Python sigue tres etapas principales:

1. **Extracción (Extract):**  
   - Recolección de datos de residuos (fuentes secundarias y registros simulados).  
   - Archivo base: `DatosResiduos.csv`.

2. **Transformación (Transform):**  
   - Limpieza y normalización de datos con librerías como `pandas` y `numpy`.  
   - Archivo procesado: `DatosResiduos_Procesados.csv`.

3. **Carga (Load):**  
   - Almacenamiento estructurado de los datos para análisis.  
   - Preparación para visualización en dashboards interactivos (Google Data Studio / Looker Studio).

El script principal es:  
- `etl_waste_data.py` → Contiene el código ETL documentado.
