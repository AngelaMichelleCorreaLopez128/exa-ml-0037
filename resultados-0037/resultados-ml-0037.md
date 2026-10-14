# Reporte de Análisis de Datos - Pandas

`Angela Correa Machine Learning pandas, NC 0037`

## 1. DataFrame Convertido
```text
    Vuelo          Destino  Precio
0  AM 401           Cancún    2500
1  VB 102      Guadalajara    1800
2  Y4 305        Monterrey    2200
3  AM 607          Tijuana    2800
4  VB 208           Mérida    2100
5  Y4 509  Puerto Vallarta    2400
```

## 2.1 Primeras Filas (head)
```text
    Vuelo      Destino  Precio
0  AM 401       Cancún    2500
1  VB 102  Guadalajara    1800
```

## 2.2 Últimas Filas (tail)
```text
    Vuelo          Destino  Precio
4  VB 208           Mérida    2100
5  Y4 509  Puerto Vallarta    2400
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Vuelo        str
Destino      str
Precio     int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   Vuelo    6 non-null      str  
 1   Destino  6 non-null      str  
 2   Precio   6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Precio'
```text
count       6.000000
mean     2300.000000
std       346.410162
min      1800.000000
25%      2125.000000
50%      2300.000000
75%      2475.000000
max      2800.000000
Name: Precio, dtype: float64
```

## 4. Ordenar Ascendente por Precio
```text
    Vuelo          Destino  Precio
1  VB 102      Guadalajara    1800
4  VB 208           Mérida    2100
2  Y4 305        Monterrey    2200
5  Y4 509  Puerto Vallarta    2400
0  AM 401           Cancún    2500
3  AM 607          Tijuana    2800
```

## 5. Ordenar Descendente por Precio
```text
    Vuelo          Destino  Precio
3  AM 607          Tijuana    2800
0  AM 401           Cancún    2500
5  Y4 509  Puerto Vallarta    2400
2  Y4 305        Monterrey    2200
4  VB 208           Mérida    2100
1  VB 102      Guadalajara    1800
```

`Angela Correa Machine Learning pandas, NC 0037`