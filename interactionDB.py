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


# insert_fitter(123441)
# set_status(123441,"К работе готов")
