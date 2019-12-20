import mysql.connector
default_authentication_plugin="mysql_native_password"
class WeatherDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="datarepresentation"
        )

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from weather_forecast"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray


    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from weather_forecast"
        cursor.execute(sql)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','datetime','windspeed']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

weatherDAO = WeatherDAO()



















#     def create(self, values):
#         cursor = self.db.cursor()
#         sql="insert into student (name, age) values (%s,%s)"
#         cursor.execute(sql, values)

#         self.db.commit()
#         return cursor.lastrowid





#     # def getAll(self):
#     #     cursor = self.db.cursor()
#     #     sql="select * from weather_forecast"
#     #     cursor.execute(sql)
#     #     result = cursor.fetchall()
#     #     return result




#     def getAll(self):
#         cursor = self.db.cursor()
#         sql="select * from weather_forecast"
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         returnArray = []
#         print(results)
#         for result in results:
#             print(result)
#             returnArray.append(self.convertToDictionary(result))

#         return returnArray


#     def findByID(self, id):
#         cursor = self.db.cursor()
#         sql="select * from student where id = %s"
#         values = (id,)

#         cursor.execute(sql, values)
#         result = cursor.fetchone()
#         return result
#     def update(self, values):
#         cursor = self.db.cursor()
#         sql="update student set name= %s, age=%s  where id = %s"
#         cursor.execute(sql, values)
#         self.db.commit()
#     def delete(self, id):
#         cursor = self.db.cursor()
#         sql="delete from student where id = %s"
#         values = (id,)

#         cursor.execute(sql, values)

#         self.db.commit()
#         print("delete done")

# weatherDAO = WeatherDAO()