import psycopg2
from read_config import importa_conexion

if __name__ == '__main__':

    try:
        string_conn = importa_conexion()
        print(string_conn)
        conn = psycopg2.connect(**string_conn)

        if conn is not None:
            print('Database connected....')

        cur = conn.cursor()


    except (Exception, psycopg2.DatabaseError) as e:
        print('Error de base de datos {}'.format(e))

    finally:
        if conn is not None:
            conn.close()