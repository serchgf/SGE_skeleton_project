import logging

import pytest
from Config.config import txt_files_path
from sge_functions.sge_functions2 import sge_functions2
from Config.config import login_data, images, files
from Config.config import images
from steps import MTC_ASGE_001_steps
from pytest import mark

import json

#Funciones globales para usar en todos lados

def leer_datos_desde_json(json_path):
    with open(json_path) as archivo:
        datos = json.load(archivo)
    return datos.values()

def cargar_datos_prueba(json_path):
    datos = leer_datos_desde_json(json_path)
    return datos


class MTC_ASGE_001_Tests:

    @pytest.mark.parametrize("data", cargar_datos_prueba(files.mtc_asge_001_json))
    @pytest.mark.demo
    def test_ASGE_001(self, data):

        print("------------------------------Test to Create Purchase Order Nacional_SINDSO")


        """TC6 ESTE TEST CASE NECESITA FACTURAS CON STATUS  'EN TRANSITO' """
        # print("Test using: "+supplier)
        sge_funct = sge_functions2()
        sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")

        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"

        MTC_ASGE_001_steps.MTC_ASGE_001_steps(sge_funct, data)

        print("Validating Purchase Order creation")
        nombre_status = "confirmada por proveedor"
        img_status_confirmada = images.img_status_confirmada_por_proveedor
        print("paso por aqui")
        if sge_funct.validar_po_status2(img_status_confirmada, nombre_status):
            sge_funct.take_screenshot("my_screenshot")
            print(f"Status {nombre_status} validado correctamente")
            print("Creando archivos: factura valida y factura invalida")
        else:
            print("Fallo validacion, estatus Incorrecto")
            sge_funct.take_screenshot("my_screenshot")
            assert False, "Fallo validacion, estatus Incorrecto"

        sge_funct.terminate_sge_session()



