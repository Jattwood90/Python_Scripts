"""
Light weight SQL database that will be used for storing API results in another script.
"""

import sqlite3
from datetime import date

#date for adding
today = date.today()

#default database arguement for functions
db = 'database'

#Create database table
def createTable(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"""CREATE TABLE {db} (
        videoID text primary key,
        YTChannelName text,
        date text,
        videoStatus text
        )""")
    conn.commit()
    conn.close()
    print('Table created!')

#Show all data in record
def show_all_data(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(f"SELECT videoID, * FROM {db}")
    objs = c.fetchall()

    for obj in objs:
        print(obj)

    conn.commit()
    conn.close()

#add a single record
def add_record(videoID, YTChannelName, today=today, videoStatus=False):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"INSERT INTO {db} VALUES (?,?,?,?)", (videoID, YTChannelName, today, videoStatus, ))
    conn.commit()
    conn.close()
    print('Data added!')

#add a list of records (list will be passed in as function arguement)
def addList(data):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.executemany(f"INSERT INTO {db} VALUES (?,?,?,?)", data, )
    conn.commit()
    conn.close()
    print('Data list added!')

#delete single line of data
def delete_data(videoID):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"DELETE from {db} WHERE videoID = (?)", (videoID, ))
    conn.commit()
    conn.close()
    print('Data has been deleted!')

def delete_channel(YTChannelName):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"DELETE from {db} WHERE YTChannelName = (?)", (YTChannelName, ))
    conn.commit()
    conn.close()
    print('Channel has been deleted!')

#lookup YT Channel Name
def lookup(YTChannelName):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"SELECT * from {db} WHERE YTChannelName = (?)", (YTChannelName, ))
    objs = c.fetchall()

    if len(objs) == 0:
        print('No data found')

    for obj in objs:
        print(obj)

def returnList(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(f"SELECT videoID, * FROM {db}")
    objs = c.fetchall()
    output = [i for i in objs]
    return output

def returnTrue(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(f"SELECT videoID, * FROM {db} WHERE videoStatus = TRUE")
    objs = c.fetchall()
    output = [i for i in objs]
    return output

def returnFalse(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(f"SELECT videoID, * FROM {db} WHERE videoStatus = FALSE")
    objs = c.fetchall()
    output = [i for i in objs]
    return output


def updateData():
    pass
    #TODO have a function that recognises changes in the dataset compared with a list

