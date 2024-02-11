CREATE TABLE TIEMPO(
    ID_TIEMPO INT PRIMARY KEY IDENTITY(1,1),
    ANIO INT
);

CREATE TABLE LUGAR(
    ID_LUGAR INT PRIMARY KEY IDENTITY(1,1),
    PAIS VARCHAR(75)
);

CREATE TABLE LONGITUD(
    ID_LONGITUD INT PRIMARY KEY IDENTITY(1,1),
    MAXIMUM_WATER_HEIGHT DECIMAL
);

CREATE TABLE TSUNAMI(
    ID_TSUNAMI INT PRIMARY KEY IDENTITY(1,1),
    TSUNAMI_EVENT_VALIDITY INT
);

CREATE TABLE HISTORIAL_TSUNAMIS(
    ID_HISTORIAL_TSUNAMIS INT PRIMARY KEY IDENTITY(1,1),
    ID_TIEMPO INT,
    ID_LUGAR INT,
    ID_TOTALES INT,
    ID_LONGITUD INT,
    ID_TSUNAMI INT,
    FOREIGN KEY (ID_TIEMPO) REFERENCES TIEMPO(ID_TIEMPO),
    FOREIGN KEY (ID_LUGAR) REFERENCES LUGAR(ID_LUGAR),
    FOREIGN KEY (ID_TOTALES) REFERENCES TOTALES(ID_TOTALES),
    FOREIGN KEY (ID_LONGITUD) REFERENCES LONGITUD(ID_LONGITUD),
    FOREIGN KEY (ID_TSUNAMI) REFERENCES TSUNAMI(ID_TSUNAMI)
);