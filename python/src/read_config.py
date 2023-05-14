from configparser import ConfigParser

def importa_conexion(): 

    configuracion = ConfigParser()

    try:
        configuracion.read('./config/configuration.conf')

        if configuracion.has_section('POSTGRES'):
            options = configuracion.options('POSTGRES')
            data_base_data = {}
            for opt in options:
                data_base_data[opt] = configuracion.get('POSTGRES', opt)

            return data_base_data

    except Exception as e:
        print('error {}'.format(e))
