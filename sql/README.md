# Base de datos `DesafioDataEntry`

# Consultas SQL

-- Repuestos del proveedor Autofix cuyo precio no se haya actualizado en el ultimo mes.

```sql
SELECT R.*
FROM Repuesto R
JOIN Proveedor P ON R.proveedor_id = P.id
LEFT JOIN Actualizacion A ON R.ultima_actualizacion_id = A.id
WHERE P.id = 4 
  AND (A.fecha < NOW() - INTERVAL 1 MONTH OR A.fecha IS NULL);

 -- Actualizar los precios de los repuestos de las marcas “ELEXA”, “BERU”, “SH”, “MASTERFILT” y “RN” incrementando un 15%
UPDATE Repuesto R
JOIN Marca M ON R.marca_id = M.id
SET R.precio = R.precio * 1.15
WHERE M.nombre IN ('ELEXA', 'BERU', 'SH', 'MASTERFILT', 'RN');

-- Obtener el promedio de precios de los repuestos por cada marca.
SELECT M.nombre AS Marca, AVG(R.precio) AS Promedio_Precio
FROM Repuesto R
JOIN Marca M ON R.marca_id = M.id
GROUP BY M.nombre;  -- Agrupa los resultados por el nombre de la marca

-- Obtener los repuestos que no tienen una descripción asignada (descripción es NULL o vacía).
SELECT *
FROM Repuesto
WHERE descripcion IS NULL OR descripcion = '';

-- Contar el número de repuestos de cada proveedor y mostrar solo aquellos proveedores que tienen al menos 1000 repuestos.
SELECT P.nombre AS Proveedor, COUNT(R.id) AS Total_Repuestos
FROM Proveedor P
JOIN Repuesto R ON P.id = R.proveedor_id
GROUP BY P.nombre
HAVING COUNT(R.id) >= 1000;

-- Obtener el repuesto más caro de cada proveedor
SELECT R.*, P.nombre AS Proveedor
FROM Repuesto R
JOIN (
    SELECT proveedor_id, MAX(precio) AS Max_Precio
    FROM Repuesto
    GROUP BY proveedor_id
) AS Max_Repuestos ON R.proveedor_id = Max_Repuestos.proveedor_id AND R.precio = Max_Repuestos.Max_Precio
JOIN Proveedor P ON R.proveedor_id = P.id;

-- Aplicar un recargo del 30% en los artículos de los proveedores AutoRepuestos Express y Automax cuyo precio sea mayor a $50000 y menor a $100000
UPDATE Repuesto R
JOIN Proveedor P ON R.proveedor_id = P.id
SET R.precio = R.precio * 1.30
WHERE P.nombre IN ('AutoRepuestos Express', 'Automax')
  AND R.precio > 50000 AND R.precio < 100000;