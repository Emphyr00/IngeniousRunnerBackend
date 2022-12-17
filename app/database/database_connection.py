import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="172.19.0.3",
            database="brain_runner",
            user="brain_runner",
            password="password",
            port="5432" )
        

    def getAllRunsByUser(self, userName):
        
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM runs INNER JOIN users ON users.id=runs.user_id WHERE users.name LIKE '{userName}';" )
        
        value = cur.fetchall()
        
        cur.close()
        
        return value
    
    def saveRun(self, userName, top, bottom, left, right, center):
        cur = self.conn.cursor()
        
        cur.execute(f"SELECT * FROM runs INNER JOIN users ON users.id=runs.user_id WHERE users.name LIKE '{userName}' AND top_field='{top}' AND bottom_field='{bottom}' AND left_field='{left}' AND right_field='{right}' AND center_field='{center}';")
        
        run = cur.fetchall()
        
        userId = self.getUserByName(userName)[0]
        
        # create new
        if (run == []):
            cur.execute(f"INSERT INTO runs (user_id, top_field, bottom_field, left_field, right_field, center_field, lose_count) VALUES ({userId}, {top}, {bottom}, {left}, {right}, {center}, 1);")
            cur.execute('commit')
        else:
            count = run[0][7] + 1
            cur.execute(f"UPDATE runs SET lose_count={count} WHERE id={run[0][0]}")
            cur.execute('commit')
            
        cur.close()
        
        return True
            
            
        
    def saveUser(self, userName):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO users (name) VALUES ('{userName}');")
        cur.execute('commit')
        
        cur.close()
        
        return True
        
    def updateUserModel(self, userName, model, featureList):
        cur = self.conn.cursor()
        userId = self.getUserByName(userName)[0]
        
        cur.execute(f"UPDATE users SET model_serialized={model}, features_list_serialized={featureList} WHERE id={userId};")
        cur.execute('commit')
        
        cur.close()
        
        return True
        
    def getUserByName(self, userName):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM users WHERE name LIKE '{userName}';" )
        
        value = cur.fetchall()
        
        if (len(value)):
            value = value[0]
        
        cur.close()
        
        return value

    def getQueue(self):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM queue ORDER BY id LIMIT 1")
        
        value = cur.fetchall()
        
        if (len(value) == 1):
            cur.execute(f"DELETE FROM queue WHERE id={value[0][0]}")
            cur.execute('commit')
        
        cur.close()
        
        return value
        
    def addToQueue(self, userName):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO queue (user_name) VALUES ('{userName}');")
        cur.execute('commit')
        
        return True
    
    def getNumberOfRunsForUser (self, userName):
        cur = self.conn.cursor()
        cur.execute(f"SELECT SUM(lose_count) FROM runs INNER JOIN users ON users.id=runs.user_id WHERE users.name LIKE '{userName}';" )
        
        value = cur.fetchall()
        
        cur.close()
        
        return value
    
    def refreshDatabase (self):
        cur = self.conn.cursor()
        
        cur.execute('DROP TABLE IF EXISTS runs;')
        cur.execute('DROP TABLE IF EXISTS users;')
        cur.execute('DROP TABLE IF EXISTS queue;')
        
        cur.execute('CREATE TABLE users (id serial PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL, model_serialized VARCHAR, features_list_serialized VARCHAR);')
        cur.execute('CREATE TABLE runs (id serial PRIMARY KEY, user_id integer REFERENCES users (id), top_field smallint NULL, bottom_field smallint NULL, left_field smallint NULL, right_field smallint NULL, center_field smallint, lose_count smallint);')
        cur.execute('CREATE TABLE queue (id serial PRIMARY KEY, user_name VARCHAR(50) NOT NULL);')
        
        cur.execute('commit')
        
        cur.close()
        
        return True
    