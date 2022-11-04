import requests
import json
import sys
import mysql.connector
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='productdb')
except mysql.connector.Error as e:
    print("Connector error ",e)
mycursor = mydb.cursor()    
data = requests.get("https://dummyjson.com/products").text
data_information=json.loads(data)
print(data_information)

for products in data_information.values():
    if(isinstance(products,int)):
            break
    for i in products:            
        price = str(i['price'])
        discout = str(i['discountPercentage'])
        rating = str(i['rating'])
        stock = str(i['stock'])
        sql = 'INSERT INTO `product`(`title`, `description`, `price`, `discount`, `rating`, `stock`, `brand`, `category`) VALUES ("'+i['title']+'","'+i['description']+'", "'+price+'","'+discout+'","'+rating+'","'+stock+'","'+i['brand']+'","'+i['category']+'")'
        mycursor.execute(sql)
        mydb.commit()
        print("Data inserted successfully", i['title'])