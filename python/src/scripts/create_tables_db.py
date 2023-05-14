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
    )
)