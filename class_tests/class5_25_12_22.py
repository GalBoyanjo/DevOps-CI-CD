import pymysql

schema_name = "freedb_DevOpsTest"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_DevOps', passwd='3R*AKs46qt$h$aR', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
# statementToExecute = "CREATE TABLE `"+schema_name+"`.`users`(`id` INT NOT NULL,`name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`));"
statementToExecute = "INSERT INTO `"+schema_name+"`.`users`(`id`,`name`) VALUES (12, 'Gal');"
cursor.execute(statementToExecute)

cursor.close()
conn.close()
