import psycopg2

class Connect_DB:
    def __init__(self):
        self.conn = psycopg2.connect(host = "localhost", dbname = "crud_db", user = "postgres",
                                     password = "admin", port = "5432")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS EMPLOYEE_INFO (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(100),
        AGE INT
        );
        ''') 
    def closing_tags(self):
        
        self.cursor.close()
        self.conn.close()


    def select(self):
        return_value = None
        self.cursor.execute('''
        SELECT * FROM EMPLOYEE_INFO;
        ''')
        return_value = self.cursor.fetchall()
        self.conn.commit()
        return(return_value)
    
    def insert(self,name, age):
        try: 
            self.cursor.execute("INSERT INTO EMPLOYEE_INFO(name,age) VALUES('%s',%d);" % (name,age))
            self.conn.commit()
            return("Successfully inserted data in the database")
        except:
            return("There's an error of inserting data into the database")
       
    

    def change(self,id,name,age):
        try:
            self.cursor.execute("UPDATE EMPLOYEE_INFO SET name = '%s', age = %d WHERE id = %d;" % (name,age,id))
            self.conn.commit()
            return("Successfully changed data in the database")
        except:
            return("There's an error in updating the data")
        
    def remove(self,id):
        try:
            self.cursor.execute("DELETE FROM EMPLOYEE_INFO WHERE id = %d;" % (id))
            self.conn.commit()
            return("Successfully deleted data in the database")
        except:
            return("There's an error in deleting the data")
    