import psycopg2
from create_tables_db import sql_create_db



conn = psycopg2.connect(database='db_test', host='172.30.0.2', port=5432, user='nico123', password='nico123')


try:
    cur =conn.cursor()

    print('La version de la base de datos es:')
    cur.execute('select version()')

    print(cur.fetchone())

    for sql in sql_create_db:
        cur.execute(sql)
        conn.commit()    

except (Exception, psycopg2.DatabaseError) as e:
    print('Se produjo una excepcion {}'.format(e))

finally:
    conn.close()


