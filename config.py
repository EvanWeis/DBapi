import os


def set_db_name(db_name: str = 'test'):
    global db_file
    db_file = db_name + ".db"

    return db_file

def get_db_path(db_file):
    dir_path = os.getcwd()
    db_path = (dir_path + '\\' + db_file)
     
    return db_path
