"""
Light weight SQl database that will be used for storing API results in another script.
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
        videoID text,
        YTChannelName text,
        date text,
        videoStatus text
        )""")
    conn.commit()
    conn.close()

#Show all data in record
def show_all_data(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(f"SELECT rowID, * FROM {db}")
    objs = c.fetchall()

    for obj in objs:
        print(obj)

    conn.commit()
    conn.close()

#add a single record
def add_record(videoID, YTChannelName, today=today, videoStatus=None):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"INSERT INTO {db} VALUES (?,?,?,?)", (videoID, YTChannelName, today, videoStatus, ))
    conn.commit()
    conn.close()

#add a list of records (list will be passed in as function arguement)
def addList(data):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.executemany(f"INSERT INTO {db} VALUES (?,?,?,?)", (data, ))
    conn.commit()
    conn.close()

#delete single line of data
def delete_data(videoID):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"DELETE from {db} WHERE videoID = (?)", (videoID, ))
    conn.commit()
    conn.close()

#lookup YT Channel Name
def lookup(YTChannelName):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"SELECT * from {db} WHERE YTChannelName = (?)", (YTChannelName, ))
    objs = c.fetchall()

    for obj in objs:
        print(obj)

