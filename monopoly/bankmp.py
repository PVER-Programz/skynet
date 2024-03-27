import firebase_admin
from firebase_admin import db
import json
import os
import time
strt = time.time()

cred_object = firebase_admin.credentials.Certificate('authson.json')
default_app = firebase_admin.initialize_app(cred_object, {
    'databaseURL':"https://mysamplecodetest-default-rtdb.asia-southeast1.firebasedatabase.app"
    })
ref = db.reference("/")

def reset_bid(noofusers, inimon):
    ref.set({})
    ref.child("data").update({f"userbet":0})
    ref.child("data").update({f"usercount":noofusers})
    ref.child("data").update({f"initialmoney":inimon})
    for x in range(1,noofusers+1):
        ref.child("players").update({f"user{x}":inimon})

def add(userno, amt):
    setamt(userno, ref.child("players").child(f"user{userno}").get()+amt)

def sub(userno,amt):
    add(userno, -amt)

def setamt(userno, amt):
    ref.child("players").child(f"user{userno}").set(amt)

def bet(amt):
    usrcnt = ref.child("data").child("usercount").get()
    for x in range(1, usrcnt+1):
        sub(x, amt)
    ref.child("data").update({f"userbet":ref.child("data").child("userbet").get()+(amt*usrcnt)})

def betwon(userno):
    add(userno, checkbet())
    ref.child("data").update({f"userbet":0})

def checkbal(userno):
    return ref.child("players").child(f"user{userno}").get()

def checkall():
    return ref.child("players").get()

def checkbet():
    return ref.child("data").child("userbet").get()

def refree():
    usrcnt = ref.child("data").child("usercount").get()
    refPocket=0
    for x in range(1, usrcnt+1):
        refPocket=refPocket + checkbal(x)
    refPocket = refPocket + ref.child("data").child("userbet").get()
    supposedValue = usrcnt * ref.child("data").child("initialmoney").get()
    if int(supposedValue)==int(refPocket):
        return True
    else:
        print(refPocket)
        print(supposedValue)
        return False
