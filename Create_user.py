from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import os
import os.path
import pathlib
os.chdir('Keys')
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import hashlib
import jwt
from time import time

from pip._vendor.distlib.compat import raw_input

def main():
    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )
    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption())
    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    qelesiPriv = str(private_key)
    qelesiPub = str(public_key)
    def Provo():
        zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
        if zgjedhja.upper() == "PO":
            CreateUser()
        else:
            print("----Procesi perfundoi-----")

    def CreateUser():
        listaUser = []
        while True:
            komanda = input("\nVendos Komanden: ")
            user = komanda[12:]
            username = user
            password = input("Enter Password : ")
            if len(password) >= 6:
                if password.isalpha() == False:
                    print()
            else:
                print("Gabim: Fjalekalimi duhet te permbaje se paku nje numer ose simbol.")
                Provo()
            password2 = input("Re-Type Password : ")
            while password != password2:
                password = input("Enter Password : ")
                password2 = input("Re-Type Password : ")
            if user.strip() != "":
                break

        a = "" + user + ".xml"
        b = "" + user + "pub.xml"

        if komanda[0:11].upper() == "CREATE-USER":
            if os.path.isfile(a):
                print("Gabim: Celesi \'"+ a +"\' ekziston paraprakisht.")
                Provo()
            elif user not in listaUser:
                listaUser.append(user)
                a = ""+ user +".xml"
                b = ""+user+".pub.xml"
                with open(a, "w+") as user:
                    user.write(qelesiPriv)
                    qelesi = "Eshte krijuar celesi privat 'keys/"+komanda[12:]+".xml'"
                    print(qelesi)
                    user.close()

                with open(b, "w+") as user:
                    user.write(qelesiPub)
                    qelesi1 = "Eshte krijuar celesi publik 'keys/" + komanda[12:] + ".pub.xml'"
                    print(qelesi1)

                    user.close()

                #-----------------------------------------------------------------------------------
                if not check_user(username):
                    if insert_User(username, password, qelesiPub, qelesiPriv):
                        print("[] Successfully Regstired")
                        print("Username :", username)
                        print("Password :", password)


                    else:
                        print("Something error")

                else:
                    print("[-] Sorry , User Registerd Before")

        
        elif komanda[0:11].upper() == "DELETE-USER":
            deleteUser(user)
        else:
            print("Ju lutem Shenoni Komanden si duhet: P.sh:Create-user Filani")

    def check_user(username):

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='shemb',
                                                 user='root',
                                                 password='')
            sql_select_Query = "select * from users where username = '{0}'".format(username)
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            if cursor.rowcount > 0:
                return True
            else:
                return False

            """
            for row in records:
                print("Id = ", row[0], )
                print("Name = ", row[1])
                print("Price  = ", row[2])
                print("Purchase date  = ", row[3], "\n")
            """

        except Error as e:
            return False

    def insert_User(username, password, public, private):
        try:
            password = hashlib.sha512(password.encode("utf-8")).hexdigest()
            connection = mysql.connector.connect(host='localhost',
                                                 database='shemb',
                                                 user='root',
                                                 password='')

            mySql_insert_query = """INSERT INTO users VALUES ("{0}", "{1}", "{2}", "{3}") """.format(username, password,
                                                                                                     public, private)

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            cursor.close()
            if (connection.is_connected()):
                connection.close()
            return True

        except mysql.connector.Error as error:
            return False
#-----------------------------------------------------------------------------------------------------------------------
# Delete-user ::::::::::

    def deleteUser(user):
        a = ""+ user +".xml"
        b = ""+user+".pub.xml"
        if os.path.isfile(b) and os.path.isfile(a):
            os.remove(b)
            os.remove(a)
            
            print("Celesi privat\'" + a +"\' u fshi me sukses.")
            print("Celesi publik \'"+b+"\' u fshi me sukses.")
            Provo()
            
        elif os.path.exists(a) and not os.path.exists(b):
            os.remove(a)
            print("Celesi privat \'"+ a +"\' u fshi me sukses.")

        elif not (os.path.exists(a)) and os.path.exists(b):
            os.remove(b)
            print("Celesi publik \'"+ b +"\' u fshi me sukses.")

        else:
            print("Celesi \'" + a + "\' nuk ekziston.")
            Provo()

    def create_token(username, password, private):

        data = {
            'username': username,
            'password': password,
            'expr': time() + 12000
        }
        token = jwt.encode(data, private, algorithm='HS256').decode('utf-8')
        return token

    def login(username, password):

        try:
            password = hashlib.sha512(password.encode("utf-8")).hexdigest()
            connection = mysql.connector.connect(host='localhost',
                                                 database='shemb',
                                                 user='root',
                                                 password='')
            sql_select_Query = "select * from users where username = '{0}' AND password = '{1}'".format(username,
                                                                                                        password)
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            if cursor.rowcount > 0:
                return [True, records]
            else:
                return [False]

        except Error as e:
            return [False]

    def insert_token(username, password, token):
        try:
            password = hashlib.sha512(password.encode("utf-8")).hexdigest()
            connection = mysql.connector.connect(host='localhost',
                                                 database='shemb',
                                                 user='root',
                                                 password='')
            check = check_user(username)
            if check:
                sql_update_query = "Update users_token set token = '{2}' where username = '{0}' AND password = '{1}'".format(
                    username, password, token)
                cursor = connection.cursor()
                cursor.execute(sql_update_query)
                connection.commit()
                cursor.close()
                if (connection.is_connected()):
                    connection.close()
                return True
            else:
                mySql_insert_query = "insert into users_token VALUES('{0}','{1}','{2}')".format(username, password,
                                                                                                token)
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                cursor.close()
                if (connection.is_connected()):
                    connection.close()
                return True
        except Error as e:
            return [False]

    CreateUser()


if __name__=="__main__":
    main()