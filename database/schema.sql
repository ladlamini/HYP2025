-- Create Detection_Type table
CREATE TABLE Detection_Type (
    Dataset_ID INTEGER PRIMARY KEY,
    DType_Name VARCHAR(50)
);

-- Create Alerts_Type table
CREATE TABLE Alerts_Type (
    Anci_Type_ID INTEGER PRIMARY KEY,
    ANCI_Local INTEGER
);

-- Create Model_Type table
CREATE TABLE Model_Type (
    Model_Tope_ID INTEGER PRIMARY KEY,
    MT_Name VARCHAR(50)
);

-- Create Model_Performance table
CREATE TABLE Model_Performance (
    Model_Performance_ID INTEGER PRIMARY KEY,
    Model_Metric DECIMAL,
    Encoding_Date DATETIME
);

-- Create InitialInclure table
CREATE TABLE InitialInclure (
    InitialInclure_ID INTEGER PRIMARY KEY,
    Intra_Name VARCHAR(50),
    Intra_p_Address VARCHAR(15),
    Data_Recorded DATETIME,
    ANCI_TYPE_ID INTEGER,
    ANCI_Key VARCHAR(50),
    FOREIGN KEY (ANCI_TYPE_ID) REFERENCES Alerts_Type(Anci_Type_ID)
);

-- Create Alerts table
CREATE TABLE Alerts (
    ANCI_ID INTEGER,
    ANCI_Type_ID INTEGER,
    ANCI_Key VARCHAR(50),
    Data_Recorded DATETIME,
    PRIMARY KEY (ANCI_ID, ANCI_Type_ID),
    FOREIGN KEY (ANCI_Type_ID) REFERENCES Alerts_Type(Anci_Type_ID)
);

-- Create ML_Model table
CREATE TABLE ML_Model (
    ML_ID INTEGER,
    Model_Performance_ID INTEGER,
    ML_Name VARCHAR(50),
    Model_Type_ID INTEGER,
    PRIMARY KEY (ML_ID, Model_Performance_ID, ML_Name, Model_Type_ID),
    FOREIGN KEY (Model_Performance_ID) REFERENCES Model_Performance(Model_Performance_ID),
    FOREIGN KEY (Model_Type_ID) REFERENCES Model_Type(Model_Tope_ID)
);

-- Create Vulnerability_Detection table
CREATE TABLE Vulnerability_Detection (
    VDL_ID INTEGER,
    Detection_Name VARCHAR(50),
    DType_ID INTEGER,
    Infrastructure_ID INTEGER,
    Alerts_ID INTEGER,
    PRIMARY KEY (VDL_ID, DType_ID, Infrastructure_ID, Alerts_ID),
    FOREIGN KEY (DType_ID) REFERENCES Detection_Type(Dissel_ID),
    FOREIGN KEY (Alerts_ID) REFERENCES Alerts(ANCI_ID)
);

-- Create Dataset table
CREATE TABLE Dataset (
    Dataset_ID INTEGER,
    ML_ID INTEGER,
    VD_ID INTEGER,
    Dataset_Name VARCHAR(50),
    PRIMARY KEY (Dataset_ID, ML_ID, VD_ID, Dataset_Name),
    FOREIGN KEY (ML_ID) REFERENCES ML_Model(ML_ID),
    FOREIGN KEY (VD_ID) REFERENCES Vulnerability_Detection(VDL_ID)
);