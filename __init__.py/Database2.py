import mysql.connector

mydb = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='1234',
                            database='team'
                            )
my_cursor = mydb.cursor()
my_cursor.execute('''
CREATE TABLE customer (
  `Ref` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Mother` VARCHAR(45) NULL,
  `Gender` VARCHAR(45) NULL,
  `PostCode` VARCHAR(45) NULL,
  `Mobile Number` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Nationality` VARCHAR(45) NULL,
  `Id_Proof` VARCHAR(45) NULL,
  `Id_Number` VARCHAR(45) NULL,
  `Address` VARCHAR(100) NULL,
  PRIMARY KEY (`Ref`));
''')
mydb.commit()
print("Table created successfully")
mydb.close()