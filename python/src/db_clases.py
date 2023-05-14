import psycopg2
from read_config import importa_conexion

class Database:
    def __init__(self, motor):
        self.motor = motor
        self._db_conectar()


    def _db_conectar(self):
        try:
            conf = importa_conexion()
            self.conn = psycopg2.connect(**conf)
            if self.conn is not None:
                print('Database conneted....')
                self.cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as e:
            print('Error de BD {}'.format(e))


    def db_select(self, query):
        self.cur.execute(query)
        return self.cur.fetchone()

    def db_update(self, query, parametros):
        self.cur.execute(query, parametros)
        self.db_commit()


    def db_insert(self, query, parametros):
        self.cur.execute(query,parametros)
        self.db_commit()

    def db_delete(self, query):
        pass

    def db_commit(self):
        self.conn.commit()

    def db_rollback(self):
        self.conn.rollback()

    def cierra_coneccion(self):
        if self.conn is not None:
            print('Se cierra la coneccion...')
            self.conn.close()

    def db_ejecuta_proc(self, procedimiento, params):
        self.cur.execute('CALL {}(%s,%s)'.format(procedimiento), params)
        return  self.cur.fetchone()



if __name__ == '__main__':
    db = Database('postgres')

    query = '''
    select version()
    '''

    final = db.db_select(query)
    print(final)

    query_1 = '''
    insert into ctr_controles_movimiento(id,descripcion, estado) values (%s,%s,%s)'''

    db.db_insert(query_1, (123,'Primer_control','AC'))

    query_2 = '''
    update ctr_controles_movimiento set estado = %s
    where id = %s'''

    db.db_update(query_2, ('IN', 123,))
    
    rta = db.db_ejecuta_proc('public.get_proc',(None, None,))
    print(rta[0], rta[1])

    db.cierra_coneccion()

