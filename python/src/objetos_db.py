sql_create_db = (
    (
        '''
        CREATE TABLE  if not exists ctr_proceso
        (
            id integer,
            fecha_inicio date,
            fecha_fin date,
            estado varchar(2),
            ultimo_workflow_id integer
        );
        '''
    ),

    (
        '''
        create table  if not exists ctr_workflow_proceso
        (
            id integer,
            id_proceso integer,
            id_workflow integer,
            estado varchar(2),
            fecha_inicio date,
            fecha_fin date
        );
        '''
    ),

    (
        '''
        create table  if not exists ctr_workflow_detalle
        (
            id integer,
            id_workflow_proceso integer,
            id_funcion integer,
            fecha_inicio date,
            fecha_fin date,
            estado varchar(2)
        );
        '''
    ),

    (
        '''
        create table  if not exists ctr_workflow
        (
            id integer,
            descripcion varchar(250),
            estado varchar(2)
        );
        '''
    ),
    (
        '''
        create table  if not exists ctr_funcion_workflow
        (
            id integer,
            id_workflow integer,
            id_funcion integer,
            estado varchar(2)
        );'''
    ),
    (
        '''create table  if not exists  ctr_funcion(
            id integer,
            nombre varchar(250),
            descripcion varchar(250),
            es_sql integer
        );'''
    ),
    (
    """
    CREATE TABLE IF NOT EXISTS ctr_controles_movimiento 
    (
        id INTEGER,
        id_workflow INTEGER,
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
    ),
    (
    """
    CREATE TABLE IF NOT EXISTS ctr_batch 
    (
        id INTEGER,
        id_control INTEGER,
        cuit INTEGER,
        cod_error INTEGER,
        observaciones varchar(2500),
        fecha_creacion time,
        usuario_creacion time
    );
    """
    ),
    (
     """
    CREATE TABLE IF NOT EXISTS loggeo 
    (
        id INTEGER not null,
        nombre varchar(2500),
        inicio INTEGER,
        fin INTEGER,
        fecha_proceso DATE, 
        parametros varchar(2500)
    );
    """   
    ),
    (
        '''
        CREATE SEQUENCE IF NOT EXISTS seq_loggeo_id
        START 10
        INCREMENT 10 
        MINVALUE 10
        OWNED BY public.loggeo.id;'''
    )
    ,
    (
        '''
        CREATE TABLE if not exists WORKFLOW
        (
            id INTEGER,
            Descripcion varchar(250),
            estado varchar(2)
        )
        '''
    )
    ,
    
    (
        '''
        CREATE TABLE if not exists PROCESO_ESTADO_WORKFLOW
        (
            id integer,
            id_workflow integer,
            fecha_inicio date,
            fecha_fin date,
            estado varchar(2)
        )
        '''
    )
    ,
    (
        '''create sequence if not exists seq_est_wkf
        START 10
        INCREMENT  10
        MINVALUE 10
        OWNED BY public.proceso_estado_workflow.id;
        '''

    ),

    (
        '''
        create sequence if not exists seq_proceso
        start 1
        increment 1
        minvalue 1
        owned by public.ctr_proceso.id;
        '''
    )
    
)