from db_clases import Database
import time
import psycopg2
from logging import Loggeo



def trae_controles(db_conn):
    query = '''select descripcion from public.ctr_controles_movimiento'''
    cursor_select = db_conn.db_select(query)
    return cursor_select

def ejecuta_control(db_conn, lista):
    if len(lista) >= 1:
        try:
            print('dentro de la funcion {} '.format(lista))
            if db_conn is not None:
                print('coneccion abiertas')
            db_conn.cur.execute('CALL public.{}(%s,%s)'.format(lista),(123,None,))
            return db_conn.cur.fetchall()
        except (Exception) as e:
            print('hubo una excepcion {}'.format(type(e)))
            db_conn.db_rollback() # Si no hacemos un rollback no continua con el siuiente procedure aunque este ok.

    


if __name__ == '__main__':

    

    db_connecion = Database('Postgres')

    logger = Loggeo(db_connecion.conn)

    lista = logger.ejecuta_proceso(trae_controles(db_connecion))
    print(lista)

    for control in lista:
        print(control[0])
        time.sleep(5)
        rta = ejecuta_control(db_connecion, control[0])
        print(rta)



    db_connecion.cierra_coneccion()