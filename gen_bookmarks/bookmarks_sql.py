# -*- coding: utf-8 -*-
import os
import sqlite3

from yield_html import make_dict, FILE

bookmark_dict = make_dict(FILE)

def connect(filename):
    create = not os.path.exists(filename)
    db = sqlite3.connect(filename)
    if create:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE bookmarks ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,"
                       "name TEXT  NOT NULL,"
                       "link TEXT  NOT NULL)")
        db.commit()
    return db

def add_links(db, _dict):
    db.text_factory = str
    cursor = db.cursor()
    for key, value in _dict.iteritems():
        cursor.execute("INSERT INTO bookmarks "
                       "(name, link)"
                       "VALUES (?, ?)",
                       (key, value))
    db.commit()
        
    
