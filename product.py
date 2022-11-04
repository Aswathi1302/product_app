import requests
import json
import sys
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='productdb')
data = requests.get("https://dummyjson.com/products").text
data_info=json.loads(data)
print(data_info)