SELECT L.PAIS AS 'Pais', AVG(HT.TOTAL_DAMAGE) AS 'Total Damage'
FROM LUGAR L
JOIN HISTORIAL_TSUNAMIS HT ON HT.ID_LUGAR = L.ID_LUGAR
WHERE HT.TOTAL_DAMAGE <> 0.00
GROUP BY L.PAIS
ORDER BY L.PAIS;