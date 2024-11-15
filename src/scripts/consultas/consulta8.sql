SELECT TOP 5
	L.PAIS AS 'Pais',
	SUM(HT.TOTAL_HOUSES_DESTROYED) AS 'Numero de casas destruidas'
FROM LUGAR L
JOIN HISTORIAL_TSUNAMIS HT ON HT.ID_LUGAR = L.ID_LUGAR
GROUP BY L.PAIS
ORDER BY SUM(HT.TOTAL_HOUSES_DESTROYED) DESC;