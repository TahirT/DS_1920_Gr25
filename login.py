import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import hashlib
import jwt
from time import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import  hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
import sys


from pip._vendor.distlib.compat import raw_input
#eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6InRhaGlyIiwicGFzc3dvcmQiOiJ0ZW1hajEyMyIsImV4cHIiOjE1OTEzOTg1MDcuNjgwMzI4Nn0.LE4sLMI1JTyyGuCH75ZJXCMsRiyMf1ID9NDhde3KiPHgktcrXCY563-iwXXys9qzGjN4NX9tld4zAPx0FGY-_jNVwHzBxxUm96X2mYadOplu8s8X90s0vqKG4ByDeSFYe7TST2Ij1MErovIm0p8CjeEJJrUyN1rwcVX5I2jUDwviMAb6lWoH7Fc7tGATQRWbesG1z3doNRpopmepGToddBFPKyaCdcOzF0ID8VRMfElvpZWpkr6r3Q-YvRAh0syo_TIGaBAfW-AOZJgBrPGDc7uo9y6rJB6_VirWQOUzj3FMBiY3RI1PSCnoondMjO9EnNtUMJDvkKtIziHMlvvCwQ


def create_token(username , password , private):

    data = {
        'username':username,
        'password':password,
        'expr': time() + 12000
    }
    token = jwt.encode(data, private, algorithm='RS256').decode('utf-8')

    return token


def check_user(username):
    
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='shemb',
                                            user='root',
                                            password='')
        sql_select_Query = "select * from users_token where username = '{0}'".format(username)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Error as e:
        return False


def login(username,password):
    
    try:
        password = hashlib.sha512(password.encode("utf-8")).hexdigest()
        connection = mysql.connector.connect(host='localhost',
                                            database='shemb',
                                            user='root',
                                            password='')
        sql_select_Query = "select * from users where username = '{0}' AND password = '{1}'".format(username,password)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        if cursor.rowcount > 0:
            return [True,records]
        else:
            return [False]

    except Error as e:
        return [False]


def insert_token(username,password,token):
    try:
        password = hashlib.sha512(password.encode("utf-8")).hexdigest()
        connection = mysql.connector.connect(host='localhost',
                                            database='shemb',
                                            user='root',
                                            password='')
        check = check_user(username)
        if check:
            sql_update_query = "Update users_token set token = '{2}' where username = '{0}' AND password = '{1}'".format(username,password,token)
            cursor = connection.cursor()
            cursor.execute(sql_update_query)
            connection.commit()
            cursor.close()
            if (connection.is_connected()):
                connection.close()
            return True
        else:
            mySql_insert_query = "insert into users_token VALUES('{0}','{1}','{2}')".format(username,password,token)
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            cursor.close()
            if (connection.is_connected()):
                connection.close()
            return True
    except Error as e:
        return [False]

komanda = raw_input("Shenoni Komanden: ")
komanda = komanda.split()
username = komanda[1]
password = raw_input("Jepni fjalekalimin: ")

with open("key1.pem", 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()

    )
public_key = private_key.public_key()

res = login(username,password)
if res[0]:
    data = res[1]
    for row in data:
        private = private_key

    token = create_token(username,password,private)
    if(insert_token(username,password,token)):
        print ("Token: ",token)

else:
    print ("Gabim: Shfrytezuesi ose fjalekalimi i gabuar.")

