import time
import psycopg2
from datetime import datetime

conn =  psycopg2.connect(database='db_test', host='172.30.0.2', port=5432, user='nico123', password='nico123')
cur = conn.cursor()

def obtiene_nombre_proceso(funcion):
    return funcion.__name__

def obtiene_next_val(sequencia):
    string = "select nextval('{}')".format(sequencia)
    cur.execute(string)
    valor = cur.fetchone()[0]
    return valor


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
        cur.execute('insert into public.loggeo(id, nombre, inicio, fin, fecha_proceso, parametros) values (%s, %s, %s, %s, %s, %s) \
            ', (secuencia,nombre_proceso,inicio,fin,fecha_proceso, (param_1, param_2)))
        conn.commit()
        return resultado
    return wrapper


def avanza_workflow(estado_workflow):
        if estado_workflow > 0 and estado_workflow < 50 :
            try:
                cur.execute('select id from public.ctr_workflow where id > %s  order by id asc limit 1',(estado_workflow,))
                siguiente_wkf = cur.fetchall()[0]
                return siguiente_wkf
            except Exception as e:
                return 10 # el primer wkf
        return 10


def estado_workflow(id_proceso):
    try:
        cur.execute('select max(id_workflow) from public.ctr_workflow_proceso where id_proceso = %s',(id_proceso,))
        id_estado_workflow = cur.fetchall()[0][0]
        if id_estado_workflow is None:
            return -1
        return id_estado_workflow
    except Exception as e:
        return -1

def inactiva_wkf(id, estado_wkf):
    print('Llamamos a inactiva')
    print(type(estado_wkf))
    if isinstance(estado_wkf, int):
        fecha_fin = datetime.now().strftime('%Y-%m-%d')
        cur.execute("update public.ctr_workflow_proceso set estado = 'IN', fecha_fin = %s where id_proceso = %s and estado in ( 'ER', 'PE')",(fecha_fin,id))
        conn.commit()
        return 1
    return 0

def inserta_wkf(id, estado_wkf_anterior, estado_wkf_nuevo):
    if isinstance(estado_wkf_anterior,int):
        rta = inactiva_wkf(id, estado_wkf_anterior)
        fecha_inicio = datetime.now().strftime('%Y-%m-%d')
        siguiente_secuencia = obtiene_next_val('seq_est_wkf')
        cur.execute('insert into public.ctr_workflow_proceso(id, id_proceso, id_workflow, estado, fecha_inicio, fecha_fin) values \
            (%s, %s, %s, %s, %s, %s)', (siguiente_secuencia, id, estado_wkf_nuevo, 'PE',fecha_inicio, None))
        conn.commit()

def ejecuta_proceso():
    pass


def finaliza_proceso(id):
    fecha_fin = datetime.now().strftime('%Y_%m-%d')
    cur.execute("UPDATE public.ctr_proceso set estado = 'IN', fecha_fin = %s where id = %s", (fecha_fin,id))
    conn.commit()



