import pymysql
from pypika import MySQLQuery as Query, Table, Parameter, functions

config_table = Table('config')
users_table = Table('users')


def get_connection(db_user, db_pass):
    """
    Establishing a connection to DB
    :return: connection variable
    """
    conn = pymysql.connect(host='127.0.0.1', port=3306, user=db_user, passwd=db_pass,
                           db='db')
    return conn


def add_user(db_user, db_pass, user_id, user_name):
    """
    Insert user to DB
    :param db_user: DB username credential
    :param db_pass: DB password credential
    :param user_id: ID of a user to insert
    :param user_name: UserName of a user to insert
    """
    # Establishing a connection to DB
    conn = get_connection(db_user, db_pass)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    query = Query.into(users_table).columns(users_table.user_name, users_table.user_id, users_table.creation_date) \
        .insert(Parameter('%s'), Parameter('%s'), functions.Now())

    cursor.execute(query.get_sql(), (user_name, user_id))
    cursor.close()
    conn.close()


def get_user(db_user, db_pass, user_id):
# def get_user(user_id):
    """
    Get UserName from DB
    :param db_user: DB username credential
    :param db_pass: DB password credential
    :param user_id: ID of a user to get data from
    :return: UserName
    """
    # Establishing a connection to DB
    conn = get_connection(db_user, db_pass)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Get user name data from table
    query = Query.from_(users_table).select(users_table.user_name).where(users_table.user_id == user_id)
    cursor.execute(query.get_sql())
    user_name = cursor.fetchone()
    cursor.close()
    conn.close()
    if user_name == None:
        return user_name
    else:
        return user_name[0]
    # return Query.from_(users_table).select(users_table.user_name).where(users_table.user_id == user_id)


def update_user(db_user, db_pass, user_id, user_name):
    """
    Update UserName on DB
    :param db_user: DB username credential
    :param db_pass: DB password credential
    :param user_id: Id of the user that will updated
    :param user_name: UserName Data to update
    """
    # Establishing a connection to DB
    conn = get_connection(db_user, db_pass)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Updating data in the table
    query = Query.update(users_table).set(users_table.user_name, user_name).where(users_table.user_id == user_id)
    cursor.execute(query.get_sql())
    cursor.close()
    conn.close()


def delete_user(db_user, db_pass, user_id):
    """
    Delete user from DB
    :param db_user: DB username credential
    :param db_pass: DB password credential
    :param user_id: Id of a user that will be deleted
    """
    # Establishing a connection to DB
    conn = get_connection(db_user, db_pass)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Delete data from table
    query = Query.from_(users_table).delete().where(users_table.user_id == user_id)
    cursor.execute(query.get_sql())
    cursor.close()
    conn.close()


def get_config(db_user, db_pass):
    """
    Configuration Data saved on DB
    1. Gateway URL
    2. Browser to use(Selenium)
    3. UserName(for API POST requests)
    :return: will return tuple with config data:
    get_config[0] - API gateway URL
    get_config[1] - Browser to test on
    get_config[2] - UserName to be insert
    """
    # Establishing a connection to DB
    conn = get_connection(db_user, db_pass)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Get config data from DB table
    query = Query.from_(config_table).select(config_table.star)
    cursor.execute(query.get_sql())
    config_data = cursor.fetchone()
    cursor.close()
    conn.close()
    return config_data


def get_all_ids(db_user, db_pass):
    """
    Get all Users Id's from DB
    :return: List of all id's from DB
    """
    # Establishing a connection to DB
    conn = get_connection(db_user, db_pass)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Get ID from DB
    query = Query.from_(users_table).select(users_table.user_id)
    cursor.execute(query.get_sql())
    all_id = cursor.fetchall()
    cursor.close()
    conn.close()
    if all_id == None:
        return all_id
    else:
        ids = [i[0] for i in all_id]
        return ids
