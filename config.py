import os

db_file = 'test.db'
dir_path = os.getcwd()

def db_path():
    
    db_path = (dir_path + '\\' + db_file)

    return db_path