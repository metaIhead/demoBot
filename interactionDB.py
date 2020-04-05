import sqlite3

def insert_fitter(user_id):
    conn = sqlite3.connect("datab.db")
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO fitters (user_id)  VALUES ("+str(user_id)+")"
        cursor.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        error_list=str(e).split(" ")
    conn.close()

def set_status(user_id,status):
    conn = sqlite3.connect("datab.db")
    cursor = conn.cursor()

    sql = "UPDATE fitters SET status = ('{}')".format(status)+" WHERE user_id = "+str(user_id)
    cursor.execute(sql)
    conn.commit()
    conn.close()

def read_status(user_id):
    conn = sqlite3.connect("datab.db")
    cursor = conn.cursor()

    sql = "SELECT status FROM fitters WHERE user_id = "+str(user_id)
    cursor.execute(sql)
    conn.commit()
    return cursor.fetchall()
    conn.close()


def read_all_users():
    conn = sqlite3.connect("datab.db")
    cursor = conn.cursor()

    sql = "SELECT user_id, status  FROM fitters"
    cursor.execute(sql)
    conn.commit()
    data=cursor.fetchall()
    conn.close()

    list=[]
    for index in data:
        obj={
            'id': index[0],
            'status': index[1],
        }
        list.append(obj)
    return list


# user_id=33477
# insert_fitter(user_id)
# set_status(user_id,"Заявку принял")
# print(read_status(user_id))
