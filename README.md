
# Clasificador AFIP App

Esta aplicación permite cargar listados de compras descargados desde AFIP y deducir automáticamente conceptos asociados a los proveedores.

## Cambios recientes:
- Se eliminaron las consultas a CUIT Online.
- Se agregaron botones para buscar información del proveedor en Google y AFIP.
- Se organizó el proyecto en carpetas (`outputs`, `logs`).

## Instalación
```
pip install -r requirements.txt
```

## Uso
```
streamlit run app.py
```

Los archivos generados se guardarán en la carpeta `outputs`.
    