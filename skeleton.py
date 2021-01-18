from hashids import Hashids
import pyotp
from pprint import pprint
from connect import Connect
from pymongo import MongoClient
import ssl 

def referral(name):
    """ Code used to generate a referral code for every single account on Fibonia """
    #Your Code Here
   
    hashids = Hashids(min_length=7, alphabet='abcdefghijklmnopqrstuvwxyz0123456789', salt = 'fibonia')

    letters = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11,
            'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21,
            'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

    #Converts name (string) to int to use it as the parameter input for the hashid function
    def alpha_to_num(name):
        sum = 0
        count = 0
        name = ''.join(c.lower() for c in name if not c.isspace())
        for i in name:
            if count % 2 == 0:
                sum += letters.get(i)
            else: 
                sum *= letters.get(i)
            count += 1
        return sum

    #numerical encoding of the name
    num = alpha_to_num(name)
    #encode
    hashid = hashids.encrypt(num)


def otp():
    """ Code used to generate a one-time password for every single appointment on Fibonia """
    #Your Code Here
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret, interval=600)
   
    # the generated otp value (6 digits)
    otp = totp.now()
    text = 'Your OTP is ' + otp
    
    # true(valid) for 10 minutes
    totp.verify(otp)

def discount():
    """ Code used to generate a discount code to be used in Fibonia """
    #Your Code Here


class Connect(object):
    @staticmethod    
    def get_connection():
        mongo_url = "mongodb+srv://gurk91:Fibonia!2345@cluster0.a5ggi.mongodb.net/test?retryWrites=true&w=majority"
        return pymongo.MongoClient(mongo_url, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

client = Connect.get_connection()
db = client.get_database('FibTest')

def select():
    """ Extracts data from a database """

    #Your Code Here
    result = db.Users.find({})
    return result

    # iterate over the results
    # for Users in cursor:
    #     pprint(Users)

    # selects the item where status is "D"
    # db.Users.find({"status": "D"})

def update(collection,id,value):
    """ Updates data in a database """
    #Your Code Here
    db.Users.update_one({})
    db.Users.update_many({})

    # updates the item with the name "paper"
    # db.Users.update_one(
    # {"item": "paper"},
    # {"$set": {"size.uom": "cm", "status": "P"},
    #  "$currentDate": {"lastModified": True}})

def delete(collection,id,value):
    """ Deletes data from a database """
    #Your Code Here
    db.Users.delete_one({})
    db.Users.delete_many({})

    # deletes the first document where status is "D"
    # db.Users.delete_one({"status": "D"})
    

def insert():
    """ Inserts new data into a database """
    #Your Code Here
    db.Users.insert_one({})
    db.Users.insert_many({})

    # example insertion input:
    # [
    # {"item": "journal",
    #  "qty": 25,
    #  "tags": ["blank", "red"],
    #  "size": {"h": 14, "w": 21, "uom": "cm"}},
    # {"item": "mat",
    #  "qty": 85,
    #  "tags": ["gray"],
    #  "size": {"h": 27.9, "w": 35.5, "uom": "cm"}},
    # {"item": "mousepad",
    #  "qty": 25,
    #  "tags": ["gel", "blue"],
    #  "size": {"h": 19, "w": 22.85, "uom": "cm"}}]


if __name__ == "__main__":
    pass