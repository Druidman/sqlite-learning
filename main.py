import sqlite3
from guy import Guy

def insert_guy(guy: Guy):
    cursor.execute("INSERT INTO guys VALUES(:first, :last, :pay)",{'first': guy.first, 
                                                                    'last': guy.last, 
                                                                    'pay': guy.pay})
    conn.commit()

def get_guys_by_lastname(lastname: str):
    cursor.execute("SELECT * FROM guys WHERE last=:last",{'last': lastname})
    return cursor.fetchall()

def update_value(value_to_update: str, value, lastname,firstname):
    cursor.execute(f"UPDATE guys SET {value_to_update}=:value WHERE last =:last AND first=:first", {
                                                                                          'first': firstname,
                                                                          'value': value,
                                                                          'last': lastname})
    conn.commit()
    
def delete_guy(lastname,firstname):
    cursor.execute("DELETE FROM guys WHERE last=:last AND first=:first",{'last': lastname,
                                                                         'first': firstname})
    conn.commit()


conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

guy1 = Guy('jan','kowalski',90000)
guy2 = Guy('chlop','kowalski',90000)

cursor.execute(

    """
    CREATE TABLE IF NOT EXISTS guys(
    first text,
    last  text,
    pay integer
    )

    """)

conn.commit()


insert_guy(guy1)
insert_guy(guy2)

print(get_guys_by_lastname(lastname='kowalski'))

update_value(value_to_update='first',value='siema',lastname='kowalski',firstname='chlop')

print(get_guys_by_lastname(lastname='kowalski'))

delete_guy(lastname='kowalski',firstname='jan')
print(get_guys_by_lastname(lastname='kowalski'))

conn.commit()



