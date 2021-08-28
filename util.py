import sqlite3, yaml
from sqlite3 import Error

DATABASE = 'database.db'

def create_connection(db_file = DATABASE):
    """ Create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_table_user():
    """ Create a table user from the create_table function
    :return:
    """
    sql_create_user_table = """CREATE TABLE IF NOT EXISTS user (
                                    id integer PRIMARY KEY,
                                    first_name text NOT NULL,
                                    last_name text NOT NULL,
                                    username text NOT NULL
                                );"""

    conn = create_connection()

    # create tables
    if conn is not None:
        # create tasks table
        create_table(conn, sql_create_user_table)
    else:
        print("Error! cannot create the database connection.")

def create_table_msg():
    """ Create a table message from the create_table function
    :return:
    """
    sql_create_user_table = """CREATE TABLE IF NOT EXISTS message (
                                    id integer NOT NULL,
                                    message text NOT NULL
                                );"""

    conn = create_connection()

    # create tables
    if conn is not None:
        # create tasks table
        create_table(conn, sql_create_user_table)
    else:
        print("Error! cannot create the database connection.")

def get_data_yaml(args):
    """ Function to load data from yaml file.

    :param args: Attribute name to be loaded your value.
    :type args: str
    :return data: Attribute value.
    :rtype: str
    """
    with open('env.yaml') as config_file:
        cfg = yaml.load(config_file, Loader=yaml.SafeLoader)
        data = cfg[args]
    config_file.close()

    return data
