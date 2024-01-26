import os
import json
import pandas as pd
from time import sleep
from utilitarios.formato import FormatoUtil as fu
from utilitarios.presentacion import PresentacionUtil as pu


class ArchivosUtil:
    
    @staticmethod
    def guardar_archivo(data: list, path: str):
        try:
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def obtener_data(ruta_devices) -> list:
        try:
            files = ArchivosUtil.files_search(".log", ruta_devices)
            result: list = []
            if files is not None:
                for file in files:
                    with open(f"{ruta_devices}\\{file}") as f:
                        result_file = json.load(f)
                        result.append(result_file)
                return result
            else:
                return None
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def files_search(extension, path) -> list:
        try:
            archivos = os.listdir(path)
            archivos_con_extension = [archivo for archivo in archivos if archivo.endswith(extension)]
            if archivos_con_extension:
                return archivos_con_extension
            else:
                return None
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def file_remove(extension, path) -> None:
        try:
            archivos = os.listdir(path)
            archivos_con_extension = [archivo for archivo in archivos if archivo.endswith(extension)]
            if archivos_con_extension is not None:
                print("\nEliminando archivos:", end="\n")
                pu.progress_bar(0, len(archivos_con_extension))
                i:int = 0
                for archivo in archivos_con_extension:
                    sleep(0.1)
                    ruta_archivo = os.path.join(path, archivo)
                    os.remove(ruta_archivo)
                    i += 1
                    pu.progress_bar(i,len(archivos_con_extension))

                print(f"\nSe eliminaron {len(archivos_con_extension)} archivos")
            else:
                print("No se encontraron archivos")
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def validar_path(path: str) -> None:
        try:
            if not os.path.exists(path):
                os.mkdir(path)
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def load_config():
        try:
            config_path = os.path.join(os.getcwd())
            with open(f"{config_path}\\config.json") as config_file:
                data = json.load(config_file)
            return data
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def move_files_to_backup(ruta_devices: str, ruta_backup: str, simulacion: int):
        try:
            files = ArchivosUtil.files_search(".log", ruta_devices)
            if files is not None:
                for file in files:
                    path_origen: str = f"{ruta_devices}\\{file}"
                    path_destino: str = f"{ruta_backup}\\simulacion_{simulacion}"
                    ArchivosUtil.validar_path(path_destino)
                    os.rename(path_origen, f"{path_destino}\\{file}")
        except Exception as error:
            fu.error_format(error)
