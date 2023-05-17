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

    )
    
)