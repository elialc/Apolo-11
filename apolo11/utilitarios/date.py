from datetime import datetime
from utilitarios.archivos import ArchivosUtil as au

class DateUtil:
    
    @staticmethod
    def obtener_datetime_actual() -> str:
        config = au.load_config()
        formato_fecha: str = config["formato_fecha"]
        return str(datetime.now().strftime(formato_fecha))


    @staticmethod
    def obtener_datetime_actual_easy_format() -> str:
        config = au.load_config()
        return str(datetime.now().strftime("%d/%m/%Y-%H:%M:%S"))