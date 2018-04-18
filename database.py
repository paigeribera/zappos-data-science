import mysql.connector
from flask import g

# credit to: https://github.com/antondalgren/Flask-mysql-boilerplate
# very helpful with getting everything set up


def connect():
    conn = mysql.connector.connect(user="USER",
                                   password="PW",
                                   host="127.0.0.1",
                                   database="DBNAME")
    return conn

# disconnects from the db


def disconnect_db():
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# handy function that makes the database results into a dictionary
def make_dicts(cursor, row):
    """
    Makes database results to a dictionary.
    :param cursor:
    :param row:
    :return:
    """
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

# makes the database and connects to it


def get_db():
    """
    :return:
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = connect()
        db.row_factory = make_dicts
    return db


def fetch_all(cur):
    """
    :param cur:
    :return:
    """
    rv = []
    row = cur.fetchone()
    while row is not None:
        rv.append(make_dicts(cur, row))
        row = cur.fetchone()
    if len(rv) == 0:
        return None
    else:
        return rv

# this function was used multiple times. this is a way for flask/python
# to connect to a mysql db. the query is written, args are passed to it


def query_db(query, args=(), one=False, post=False):
    """
    Args must be sent as a tuple, if you have one argument pass it as (value,)
    :param query:
    :param args:
    :param one:
    :return:
    """
    db = get_db()
    cur = db.cursor()
    cur.execute(query, args)
    rv = fetch_all(cur)

    cur.close()
    db.commit()
    if post and cur.lastrowid:
        return cur.lastrowid
    return (rv[0] if rv else None) if one else rv
