from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"


    @classmethod
    def create_table(cls):
        #create a new table to persist the attributes of the department
        # ...instances

        sql = """
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()



    @classmethod
    def drop_table(cls):
    #drop the table that persists the attributes of the department
        # ...instances
        sql = """


            DROP TABLE IF EXISTS departments;
            
            """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        #insert row wit name and location values of the current department instance
        #update the id attribute with the primary key value of new row

        sql ="""
        INSERT INTO departments (name, location)
        VALUES (?,?)
            """
        CURSOR.execute(sql,(self.name,self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid


    @classmethod
    def create(cls, name, location):
        #initialize a new department instance and save the object to the database

        department = cls(name, location)
        department.save()
        return department

    def update(self):
        #update the row in the database with the name and location of the current department instance
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
                """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        #delete the tablent instance
        sql = """
            DELETE FROM departments
            where id = ?
            """    
        CURSOR.execute(sql, (self.id,))
        CONN.commit()