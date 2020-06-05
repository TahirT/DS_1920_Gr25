import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import hashlib
import jwt
from time import time
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import  hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
import sys
def sign_token(token):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='shemb',
                                            user='root',
                                            password='')
        sql_select_Query = "select * from users_token where token = '{0}'".format(token)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        if cursor.rowcount > 0:
            return [True,records]
        else:
            return [False]

    except Error as e:
        return [False]

def get_public_key_from_db(username,password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='shemb',
                                            user='root',
                                            password='')
        sql_select_Query = "select * from users where username = '{0}' AND password = '{1}'".format(username,password)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in records:
                return [True,row[2]]
        else:
            return [False]

    except Error as e:
        return [False]

token =input("Token : ")
res = sign_token(token)
with open("key1.pem", 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()

    )
public_key = private_key.public_key()
if res[0]:
    data = res[1]
    for row in data:
        username = row[0]
        print("User: "+username)
        password = row[1]
        sign = row[2] # token

        public = public_key
        if public:

            sign_data = jwt.decode(sign, public, algorithm='RS256')
            print(sign_data)
            expr = sign_data['expr']
            if(expr > time()):
                print ("User :",username)
                print ("Token eshte Valid")
                datatime = datetime.fromtimestamp(expr)
                print ("Skadimi :",datatime)
            else:
                print (" Tokeni ka skaduar")
                
        else:
            print ("Diqka error")
else:
    print ("Token invalid")