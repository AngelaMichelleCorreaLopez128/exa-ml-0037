# Angela Correa NC = 0037
# Angela Correa NC = 0037
import sys
import os
import io
import importlib
import pandas as pd

# 1. Obtener la ruta absoluta de la carpeta donde se encuentra este script
ruta_script = os.path.dirname(os.path.abspath(__file__))

# 2. Agregar la subcarpeta hermana 'datos-de-entrada-ml-0037' al sys.path
subcarpeta_datos = os.path.abspath(os.path.join(ruta_script, '..', 'datos-de-entrada-ml-0037'))
sys.path.append(subcarpeta_datos)

# 3. Importar dinámicamente 'dicc-0037' (evita SyntaxError por el guion en el nombre)
dicc_0037 = importlib.import_module("dicc-0037")

print("Angela Correa Machine Learning pandas, NC 0037")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Angela Correa Machine Learning pandas, NC 0037"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# Extraer el diccionario del módulo importado
if hasattr(dicc_0037, "datos_productos"):
    datos = dicc_0037.datos_productos
else:
    # Si no se llama datos_productos, toma la primera variable definida en el archivo
    vars_modulo = [getattr(dicc_0037, a) for a in dir(dicc_0037) if not a.startswith("__") and not callable(getattr(dicc_0037, a))]
    datos = vars_modulo[0]

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(datos)

# Limpiar espacios invisibles en nombres de columnas
df.columns = df.columns.str.strip()

registrar("1. DataFrame Convertido", df)

# Identificar columnas automáticamente (sin importar si están en mayúsculas o minúsculas)
col_precio = next((c for c in df.columns if c.lower() == 'precio'), df.columns[0])
col_stock = next((c for c in df.columns if c.lower() in ['stock', 'cantidad', 'inventario']), df.columns[-1])

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Precio)
registrar(f"3. Estadísticas Generales de la Columna '{col_precio}'", df[col_precio].describe())

# 4. Ordenar Ascendente por Precio
df_asc_precio = df.sort_values(by=col_precio, ascending=True)
registrar(f"4. Ordenar Ascendente por {col_precio}", df_asc_precio)

# 5. Ordenar Descendente por Stock
df_desc_stock = df.sort_values(by=col_stock, ascending=False)
registrar(f"5. Ordenar Descendente por {col_stock}", df_desc_stock)

# 7. Guardar el archivo resultados-ml-0037.md dentro de resultados-0037
carpeta_resultados = os.path.abspath(os.path.join(ruta_script, '..', 'resultados-0037'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0037.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Angela Correa Machine Learning pandas, NC 0037")