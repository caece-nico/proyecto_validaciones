import psycopg2

sql_create_db = (
    (
    """
    CREATE TABLE IF NOT EXISTS ctr_controles_movimiento 
    (
        id INTEGER,
        descripcion varchar(2500),
        estado varchar(2)
    );
    """
    ),
    (
    """
    CREATE TABLE IF NOT EXISTS ctr_controles_resultado 
    (
        id INTEGER,
        id_control INTEGER,
        resultado varchar(1),
        observaciones varchar(2500),
        fecha_creacion date,
        usuario_creacion varchar(250),
        fecha_ult_mod date,
        usaurio_ult_mod varchar(250)
    );
    """
    )
)


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


