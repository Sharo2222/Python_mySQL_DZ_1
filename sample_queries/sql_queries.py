def create_db(name):
    COMMAND = fr"CREATE DATABASE {name};"
    return COMMAND

def create_table(name):
    COMMAND = fr"""CREATE TABLE {name}
            (Id INT NOT NULL PRIMARY KEY,
            Name VARCHAR(50) NOT NULL UNIQUE,
            Type TINYINT(1) NOT NULL,
            Color VARCHAR(50) NOT NULL,
            Calory DECIMAL(5, 2) NOT NULL,
            Comment VARCHAR(100)
            )"""
    return COMMAND

def insert_db(table, columns, data):
    COMAND = fr"""INSERT INTO {table} {columns} VALUES {data};"""
    return COMAND

def get_data(name):
    COMMAND = fr"""SELECT * FROM {name};"""
    return COMMAND