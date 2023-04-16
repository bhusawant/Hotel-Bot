import mysql.connector

my_db = mysql.connector.connect(
                        host = 'localhost',
                        user = 'root',
                        password = '1234',
                        database = 'team'
                            )

my_cursor = my_db.cursor()

my_cursor.execute("""CREATE TABLE `team`.`csignup` (
  `Full Name` VARCHAR(45) NOT NULL,
  `Email Id` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Email Id`));""")

my_cursor.commit()
my_cursor.close()