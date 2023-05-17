import time
import psycopg2
from datetime import datetime

conn =  psycopg2.connect(database='db_test', host='172.30.0.2', port=5432, user='nico123', password='nico123')
cur = conn.cursor()

def obtiene_nombre_proceso(funcion):
    return funcion.__name__

def obtiene_next_val():
    cur.execute("select nextval('seq_loggeo_id')")
    return cur.fetchone()


def insert_loggeo(funcion):
    def wrapper(*args, **kwargs):
        fecha_proceso = datetime.now()
        param_1 = [param for param in args]
        param_2 = [f'{v,i}' for v , i in kwargs.items()]
        nombre_proceso = obtiene_nombre_proceso(funcion)
        inicio = time.process_time()
        resultado = funcion(*args, **kwargs)
        fin = time.process_time()
        secuencia = obtiene_next_val()
        cur.execute('insert into public.loggeo(id, nombre, inicio, fin, fecha_proceeso, parametros) values (%s, %s, %s, %s, %s, %s) \
            ', (secuencia,nombre_proceso,inicio,fin,fecha_proceso, (param_1, param_2)))
        conn.commit()
        return resultado
    return wrapper


def avanza_workflow(funcion, estado):
    pass

def estado_workflow(funcion):
    pass

def ejecuta_proceso():
    pass



if __name__ == '__main__':

    if conn is not None:
        cur.execute('Select * from public.ctr_controles_movimiento')
        print(cur.fetchall())
        print('Hay conexion')

@insert_loggeo
def ejecuta(a,b):
    return a +b

datos = ejecuta(1,5)
print(datos)