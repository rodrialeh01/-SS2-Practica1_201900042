DECLARE @cols AS NVARCHAR(MAX);
DECLARE @query AS NVARCHAR(MAX);

-- Obtener la lista de años únicos
SELECT @cols = COALESCE(@cols + ', ', '') + QUOTENAME('ANIO' + CAST(ROW_NUMBER() OVER (ORDER BY ANIO) AS VARCHAR))
FROM (SELECT DISTINCT ANIO FROM TIEMPO) AS A
ORDER BY ANIO;

-- Construir la consulta dinámica
SET @query = 'SELECT PAIS, ' + @cols + '
              FROM (
                SELECT L.PAIS, 
                       T.ANIO, 
                       ''ANIO'' + CAST(ROW_NUMBER() OVER (PARTITION BY L.PAIS ORDER BY T.ANIO) AS VARCHAR) AS ANIO_COL
                FROM LUGAR L
                LEFT JOIN HISTORIAL_TSUNAMIS HT ON L.ID_LUGAR = HT.ID_LUGAR
                LEFT JOIN TIEMPO T ON HT.ID_TIEMPO = T.ID_TIEMPO
              ) AS src
              PIVOT (
                MAX(ANIO) FOR ANIO_COL IN (' + @cols + ')
              ) AS pivoted
              ORDER BY PAIS;';

-- Ejecutar la consulta dinámica
EXECUTE(@query);
