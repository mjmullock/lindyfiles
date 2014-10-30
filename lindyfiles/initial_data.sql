--Some kind of header here about how to run this? like #!/usr/bin/sqlite3 ???

BULK INSERT events
FROM 'Swing_Dance_Events.csv' --might have to add path
WITH
( 	FIRSTROW = 2,
    FIELDTERMINATOR = ',',  --CSV field delimiter
    ROWTERMINATOR = '\n',   --Use to shift the control to next row
    TABLOCK --I don't know what this does but the example I found online used it
)

BULK INSERT pros
FROM 'Pro_Dancers.csv' --might have to add path
WITH
( 	FIRSTROW = 2,
    FIELDTERMINATOR = ',',  --CSV field delimiter
    ROWTERMINATOR = '\n',   --Use to shift the control to next row
    TABLOCK --I don't know what this does but the example I found online used it
)