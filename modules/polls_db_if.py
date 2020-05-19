#!/usr/bin/python3

import pymysql

db_host = "127.0.0.1"
db_user = "root"
db_pass = "563555"

db_name = "POLL"
poll_table_name = "Polls"
poll_answ_table_name = "Choises"

add_poll_query = """
INSERT INTO `POLL`.`Polls` (`title`) VALUES ('{title}')
"""

add_choise_query = """
INSERT INTO `POLL`.`Choises` (`poll_id`, `answer`) VALUES ('{poll_id}', '{choise}')
"""

get_polls_query = """
SELECT * FROM POLL.Polls
"""

get_poll_query = """
SELECT * FROM POLL.Polls WHERE id={id}
"""

get_poll_choises_query = """
SELECT * FROM POLL.Choises WHERE poll_id={id}
"""

poll_query = """
UPDATE `POLL`.`Choises`
SET `percent` = `percent` + 1
WHERE `id` = {id};
"""

def get_last_id(cursor):
    cursor.execute("select LAST_INSERT_ID()")
    return cursor.fetchone()['LAST_INSERT_ID()']


def add_choise(poll_id, choise):
    connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, db=db_name,
                charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:
        cursor.execute(add_choise_query.format(**locals()))

        connection.commit()
    except Exception as e:
        print("Exeception occured:{}".format(e))
        connection.rollback()
    finally:
        connection.close()



def add_poll(title, choises):
    connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, db=db_name,
                charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:
        cursor.execute(add_poll_query.format(**locals()))
        poll_id = get_last_id(cursor)

        for choise in choises:
            cursor.execute(add_choise_query.format(**locals()))

        connection.commit()
    except Exception as e:
        print("Exeception occured:{}".format(e))
        connection.rollback()
    finally:
        connection.close()



def get_polls():
    connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, db=db_name,
                charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    result = []

    try:
        cursor.execute(get_polls_query)
        polls = cursor.fetchall()

        for poll in polls:
            cursor.execute(get_poll_choises_query.format(id=poll['id']))
            choises = cursor.fetchall()

            choises = ({'answer':i['answer'], 'percent':i['percent'], 'id':i['id']} for i in choises)
            result.append( {'title':poll['title'], 'choises':choises} )


    except Exception as e:
        print("Exeception occured:{}".format(e))
        connection.rollback()
    finally:
        connection.close()
        
    return tuple(result)



def get_poll_by_id(id):
    connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, db=db_name,
                charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    result = ()

    try:
        cursor.execute(get_poll_query.format(**locals()))
        poll = cursor.fetchone()

        cursor.execute(get_poll_choises_query.format(id=poll['id']))
        choises = cursor.fetchall()

        choises = ({'answer':i['answer'], 'percent':i['percent'], 'id':i['id']} for i in choises)
        result = {'title':poll['title'], 'choises':choises}


    except Exception as e:
        print("Exeception occured:{}".format(e))
        connection.rollback()
    finally:
        connection.close()

    return result

def poll(choise_id):
    connection = pymysql.connect(host=db_host, user=db_user, password=db_pass, db=db_name,
                charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:
        cursor.execute(poll_query.format(id=choise_id))
        connection.commit()

    except Exception as e:
        print("Exeception occured:{}".format(e))
        connection.rollback()
    finally:
        connection.close()