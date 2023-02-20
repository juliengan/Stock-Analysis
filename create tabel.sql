IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'StockTable') AND type in (N'U'))
BEGIN
    CREATE TABLE StockTable (
        Date DATE,
        High FLOAT,
        Low FLOAT,
        [Open] FLOAT,
        [Close] FLOAT,
        Volume FLOAT,
        "Adj Close" FLOAT,
        "company_name" VARCHAR(255)
    );
END