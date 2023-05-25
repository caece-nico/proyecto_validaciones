from objetos_db import sql_create_db

def crea_base_de_datos(conn, cur):
    for obj in sql_create_db:
        try:
            cur.execute(obj)
            conn.commit()
        except Exception as e:
            conn.rollback()



