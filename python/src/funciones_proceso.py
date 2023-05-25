from  datetime import datetime

def ejecuta_proceso(conn, cur, fecha_proceso):
    try:
        print(fecha_proceso)
        cur.execute("select id, estado, ultimo_workflow_id from public.ctr_proceso where fecha_inicio >= %s and ( estado <> 'IN')",(fecha_proceso,))
        id, estado, ultimo_workflow_id = cur.fetchone()
        return (id, estado, ultimo_workflow_id)
    except Exception as e:
         return(-1, -1, -1)
      

def carga_nuevo_proceso(conn, cur):
    try:
        fecha_hoy = datetime.now().strftime('%Y-%m-%d')
        cur.execute("select nextval('seq_proceso')")
        proximo_valor = cur.fetchone()
        cur.execute('insert into public.ctr_proceso(id, fecha_inicio, fecha_fin, estado, ultimo_workflow_id) values(%s, %s, %s, %s, %s) returning id',\
            (proximo_valor,fecha_hoy, None,'PE',10))
        conn.commit()
        #id = cur.fetchall()
        return proximo_valor 
    except Exception as e:
        print(e)
        


def carga_nuevo_workflow(conn, cur):
    try:
        proximo_valor = cur.execute("select nextvalue('seq_est_wkf')")
        fecha_inicio = datetime.now()
        fecha_fin = None
        estado = 'AC'
    except Exception as e:
        pass
        