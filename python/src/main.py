import psycopg2
from datetime import datetime, timedelta
from crea_objetos_db import crea_base_de_datos
from funciones_proceso import ejecuta_proceso, carga_nuevo_proceso
from funciones_importantes import estado_workflow, avanza_workflow, inserta_wkf, finaliza_proceso
from collections import namedtuple



conn = psycopg2.connect(database='db_test', host='172.30.0.2', port=5432, user='nico123', password='nico123')

if __name__ == '__main__':
    print('Iniciamos el proceso')

##Paso 1 crea todas las tablas.
    try:
        cur =conn.cursor()
        print('La version de la base de datos es:')
        cur.execute('select version()')

        print(cur.fetchone())

        crea_base_de_datos(conn, cur)  

    except (Exception, psycopg2.DatabaseError) as e:
        print('Se produjo una excepcion {}'.format(e))

#Paso dos, termina si re-ejecuta un proceso trunco o inicia uno nuevo

    try:
        conn.commit()
        proceso_hoy = namedtuple('proceso', ['id', 'estado', 'ultimo_workflow_id'])
        fecha_hoy = datetime.now().strftime('%Y-%m-%d')
        dato =  ejecuta_proceso(conn, cur, fecha_hoy)
        #devuelve -1 si es proecso nuevo.
        proceso_hoy.id = dato[0]
        proceso_hoy.estado = dato[1]
        proceso_hoy.ultimo_workflow_id = dato[2]

        conn.commit()

        print(proceso_hoy.id)

        if proceso_hoy.id > 0:
            print(proceso_hoy.id)
            print('Hay proceso existente')
            estado_wkf = estado_workflow(proceso_hoy.id)
            print(estado_wkf)
            siguiente_wkf = avanza_workflow(estado_wkf)
            print(siguiente_wkf)

            rta_avanza_wkf = inserta_wkf(proceso_hoy.id, estado_wkf, siguiente_wkf)

            finaliza_proceso(proceso_hoy.id)

        else:
            #Es nuevo proceso
            id_sistema = carga_nuevo_proceso(conn, cur)
            estado_wkf = estado_workflow(id_sistema)

            #Sebamos que al ser nuevo proceso no tiene workflow activo
            siguiente_workflow = avanza_workflow(estado_wkf)
            #print(siguiente_workflow)

            rta_avanza_wkf = inserta_wkf(id_sistema, estado_wkf, siguiente_workflow)

            finaliza_proceso(id_sistema)
    except Exception as e:
        print(e)