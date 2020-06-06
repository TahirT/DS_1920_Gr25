
import hashlib
import jwt
import base64
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from time import time
from Crypto.Cipher import DES
from Crypto import Random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def verifiy_sign_rsa(public_key , message , sign,sender):

    with open('key1.pem','rb') as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()

        )
        pubkey = private_key.public_key()


    message = message.encode('utf-8')
    xy(sender)
    prehashed_msg = hashlib.sha256(message).hexdigest()
    arr = prehashed_msg.encode('utf-8')
    decoded_sig = base64.b64decode(sign)

    try:
        pubkey.verify(
            decoded_sig,
            arr,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256())
        return False
        sys.exit(0)
    except:
        return True

def sign_token(token):
    connection = mysql.connector.connect(host='localhost',
                                            database='shemb',
                                            user='root',
                                            password='')
    sql_select_Query = "select u.username,u.public_key,u.private_key from users_token as ut , users as u where u.username = ut.username AND token = '{0}'".format(token)
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    if cursor.rowcount > 0:
        return [True,records]
    else:
        return [False]
def xy(sender):
    try:
        merr = open(sender + "_public_key.pem")
        if merr.mode == "r":
            print("Nenshkrimi: Valid")
    except:
        print("Mungon Qelesi Publik "+sender)


def DES_decrypt(cipher,key,iv):
    block_size = DES.block_size
    d = DES.new(key,DES.MODE_CBC,iv)
    return d.decrypt(cipher).decode('ascii')

def get_all_messages(username):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='shemb',
                                            user='root',
                                            password='')
        sql_select_Query = "select * from messages Where receiver_username = '{0}'".format(username)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        if cursor.rowcount > 0:
            return [True,records]
        else:
            return [False]

    except Error as e:
        return [False]


def pad_msg(msg):
    while len(msg) % 8 != 0:
        msg += "X"
    return msg
def DES_decrypt(cipher,key,iv):
    block_size = DES.block_size
    d = DES.new(key,DES.MODE_CBC,iv)
    return d.decrypt(cipher).decode('ascii')

def decrypt_with_rsa(encrypted,private_key):
    with open(private_key, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message



token = input("Token : ")

res = sign_token(token)
check = res[0]
if not check:
    print ("[-] Invalid Token")
    exit(0)

data = res[1]
for row in data:
    username = row[0]
    public_key = row[1]
    private_key = row[2]


data = get_all_messages(username)
#for row in data:
 #   sender = row[0]
  #  msg = row[1]
   # Receiver = row[2]
    # sender_public_key = row[3]



if data[0]:
    sender = data[1]
    for row in sender:
        sender_username = row[0]
        sender_username = sender_username[1:].strip("'")
        print("Derguesi: " + sender_username)
        msg = row[1]
        Receiver = row[2]  # pranuesi
        print("Pranuesi: " + Receiver)
        sender_public_key = row[3]

    msg = msg.split(".")
    sign = base64.b64decode(msg[5])
    msg_enc_with_des = msg[3].encode('utf-8')
    msg_enc_with_des = msg_enc_with_des[1:]
    msg_enc_with_des = base64.b64decode(msg_enc_with_des)
    sender = base64.b64decode(msg[4])
    iv = msg[1].encode('utf-8')
    iv = iv[1:]
    iv = base64.b64decode(iv)
    key = msg[2].encode('utf-8')
    key = key[1:]
    key = base64.b64decode(key)



    f = open("temp_sender_public_key.pem","w")
    f.write(sender_public_key)
    f.close()
    msg_dec = DES_decrypt(msg_enc_with_des,key,iv)

    mesazhi = msg_dec.strip("X")
    print("Mesazhi: "+ mesazhi)

    if not verifiy_sign_rsa("temp_sender_public_key.pem" , msg_dec , sign,sender_username):
        print ("[-] Sign is Invalid")
        exit(0)


    f = open("temp_private_key.pem","w")
    f.write(private_key)
    f.close()


