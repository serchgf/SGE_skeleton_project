import logging
import random
import allure
#from pytest_html_reporter import attach
import pyperclip
from allure_commons.types import AttachmentType
from Config.config import txt_files_path
from Config.config import login_data
from Config.config import data_sftp_connection
from Config.config import files
from Config.config import images
from Config.connections import sftp_connection
import os
import pyautogui as pa
import subprocess
import time
import datetime
import shutil
from pyperclip import paste
import csv
import pysftp

class Po_internacional:

    def __init__(self, num_po: str, inv_po: str, num_pedimento: str, num_MUP: str, num_papeleta: str, status_previo: str, status_actual: str):
        #self.__Index = Index
        self.__num_po = num_po
        self.__inv_po = inv_po
        self.__num_pedimento = num_pedimento
        self.__num_MUP = num_MUP
        self.__num_papeleta = num_papeleta
        self.__status_previo = status_previo
        self.__status_actual = status_actual

    def obtener_num_po(self):
        return self.__num_po
    def obtener_inv_po(self):
        return self.__inv_po
    def obtener_num_pedimento(self):
        return self.__num_pedimento
    def obtener_num_MUP(self):
        return self.__num_MUP
    def obtener_num_papeleta(self):
        return self.__num_papeleta
    def obtener_status_previo(self):
        return self.__status_previo
    def obtener_status_actual(self):
        return self.__status_actual
    def actualizar_num_po(self, num_po: str):
        self.__num_po = num_po
    def actualizar_inv_po(self, inv_po: str):
        self.__inv_po = inv_po
    def actualizar_num_pedimento(self,num_pedimento: str):
        self.__num_pedimento = num_pedimento
    def actualizar_num_MUP(self, num_MUP: str):
        self.__num_MUP = num_MUP
    def actualizar_num_papeleta(self, num_papeleta: str):
        self.__num_papeleta = num_papeleta
    def actualizar_status_previo(self, status_previo: str):
        self.__status_previo = status_previo
    def actualizar_status_actual(self, status_actual: str):
        self.__status_actual = status_actual

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"num_po={self.__num_po}, inv_po={self.__inv_po}, num_pedimento={self.__num_pedimento}, num_papeleta={self.__num_papeleta}, num_MUP={self.__num_MUP}, status_previo={self.__status_previo}, status_actual={self.__status_actual}"

class Po_nacional:

    def __init__(self, num_po: str, inv_po: str, status_previo: str, status_actual: str):
        #self.__Index = Index
        self.__num_po = num_po
        self.__inv_po = inv_po
        self.__status_previo = status_previo
        self.__status_actual = status_actual

    def obtener_num_po(self):
        return self.__num_po
    def obtener_inv_po(self):
        return self.__inv_po
    def obtener_status_previo(self):
        return self.__status_previo
    def obtener_status_actual(self):
        return self.__status_actual
    def actualizar_num_po(self, num_po: str):
        self.__num_po = num_po
    def actualizar_inv_po(self, inv_po: str):
        self.__inv_po = inv_po

    def actualizar_status_previo(self, status_previo: str):
        self.__status_previo = status_previo
    def actualizar_status_actual(self, status_actual: str):
        self.__status_actual = status_actual

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"num_po={self.__num_po}, inv_po={self.__inv_po} status_previo={self.__status_previo}, status_actual={self.__status_actual}"


class sge_functions2:
    img_pantalla_inicial = images.img_pantalla_inicial
    img_error_connection = images.img_error_connection
    img_inicio_orden_de_compra = images.img_inicio_orden_de_compra
    img_consulta_orden_de_compra = images.img_consulta_orden_de_compra
    img_confirmacion_colocada = images.img_confirmacion_colocada
    img_header_orden_de_compra = images.img_header_orden_de_compra
    img_status_confirmada_por_proveedor = images.img_status_confirmada_por_proveedor


    #############
    img_promociones = images.img_promociones
    img_promociones2 = images.img_promociones2
    img_atraso = images.img_error_atraso_importante
    img_gdl = images.img_error_gdl
    #############

    close_as = ""
    route_image = ""
    po_seleccionada = ""

    def create_report_directory(self):
        main_report_dir = 'Reports/SGE_PO_Test_report_' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M/")
        """main_report_dir = 'images_report/SGE_PO_Test_report ' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S/")"""
        return main_report_dir

    def sge_connection(self, username, ip, password):
        try:
            connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)
            subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            time.sleep(3)
        except:
            print("Connection Failed...\nCheck your credentials access...")

    def validate_sge_connection(self):
        time.sleep(1)
        s = pa.locateOnScreen(self.img_pantalla_inicial)
        e = pa.locateOnScreen(self.img_error_connection)
        if s is not None:
            # print("Connection Successful!!")
            return True

        elif e is not None:
            time.sleep(1)
            message = "Connection Failed"
            self.take_screenshot(message)
            # print("Error Found, Connection Failed!!")
            return False, "Error Found, Connection Failed"
        else:
            assert False, "Error connection no defined"

    def crear_objeto_po_internacional(self):
        po_internacional_obj = Po_internacional("", "", "", "", "", "Sin Status", "")
        return po_internacional_obj

    def crear_objeto_po_Nacional(self):
        po_internacional_obj = Po_nacional("", "",  "Sin Status", "")
        return po_internacional_obj

    def take_screenshot(self, message):
        logging.info("Taking screenshot")
        print("taking screenshot " + message)
        img_name = f"my_screenshot.png"
        pa.screenshot(f"Screenshots/{img_name}")
        pa.screenshot(f"{files.screenshot_folder}{images.img_allure_screenshot_name}")
        rr = os.getcwd()+"\\Screenshots\\my_allure_screenshot.png"
        cadena = "".join(rr)
        with open(cadena, "rb")as img_file:
            f = img_file.read()
            #b = bytearray(f)
        allure.attach(f, name="para_Allure_report", attachment_type=AttachmentType.PNG)



    def close_sge_session(self, close_as):
        pa.press('enter')
        pa.hotkey('alt', 'f4')
        if close_as != 0:
            pa.press('enter')
        else:
            pass

    def validating_po(self):
        time.sleep(1)
        try:
            coord_xy = pa.locateOnScreen(self.img_confirmacion_colocada)
            if coord_xy != "":
                print("PO Created successfully")
                message = "PO_successful"
                self.take_screenshot(message)
                # self.create_inv_txt_file()
                self.close_as = 0
                return True
        except:
            print("An error has occurred, PO no created")
            message = "Test_failed"
            time.sleep(1)
            self.take_screenshot(message)
            assert False, "An error has occurred, PO no created"



    def obtener_fecha(self):
        fecha = str(datetime.datetime.now())
        fecha = fecha.split(".")
        final = ""
        if ":" in fecha[0]:
            nueva = fecha[0].replace(":", "h_", 1)
            semi = nueva.replace(":", "min_", 2)
            final = semi + "s_"
            final = final.replace(" ", "_")
        return final

    def error_screenshot(self):
        message = "connection_error"
        self.take_screenshot(message)

    def terminate_sge_session(self):
        print("Test finished...")
        self.close_sge_session(self.close_as)
        print("Session terminated")

    def move_to_report_dir(self, img_to_move, path_to_move):
        try:
            shutil.move(f"screenshots/my_screenshot.png", f"{path_to_move}/{img_to_move}")
            file_source = files.directory_tmp_file
            file_destination = path_to_move
            copy_file_destination = files.valid_inv_confirmed_po_file
            get_files = os.listdir(file_source)
            for f in get_files:
                try:
                    #shutil.copy(file_source + f, copy_file_destination + f)
                    shutil.move(file_source + f, file_destination + f)
                except:
                    print("Error, INV file no Generated")
        except:
            self.take_screenshot("my_screenshot.png")
            shutil.copy(f"screenshots/my_screenshot.png", f"{path_to_move}/{img_to_move}")

        return f"images_report/{img_to_move}"

    def promociones_y_atrasos(self):

        gdl = pa.locateOnScreen(self.img_gdl)
        atraso = pa.locateOnScreen(self.img_atraso)
        p2 = pa.locateOnScreen(self.img_promociones2)
        p = pa.locateOnScreen(self.img_promociones)
        if atraso is not None or p is not None or p2 is not None or gdl is not None:
            return True
        else:
            return False

    def sugerencia_CEDI(self):
        time.sleep(2)
        gdl = pa.locateOnScreen(self.img_gdl)
        if gdl is not None:
            pa.press('s')



    def pegar_num_inv_po(self):
        print(f"pegando numero numero de INV: {self.po_seleccionada}")
        pa.typewrite(f"INV{self.po_seleccionada}")

    def pegar_num_po(self):
        print(f"pegando numero numero de PO: {self.po_seleccionada}")
        pa.typewrite(f"{self.po_seleccionada}")


    def mover_facturas(self, num_po_seleccionada: str, path_directorio_origen: str, path_directorio_destino: str):
        try:
            shutil.move(f"{path_directorio_origen}INV-{num_po_seleccionada}.txt",
                        f"{path_directorio_destino}INV-{num_po_seleccionada}.txt")
        except:
            print("no se movio el archivo")

    def copiar_facturas(self, num_po_seleccionada: str, path_directorio_origen: str, path_directorio_destino: str):
        try:
            shutil.copy(f"{path_directorio_origen}INV-{num_po_seleccionada}.txt",
                        f"{path_directorio_destino}INV-{num_po_seleccionada}.txt")
        except:
            print("no se copio el archivo")

    def copiar_archivo(self, nombre_archivo: str, path_directorio_origen: str, path_directorio_destino: str, filename_destiny: str):
        try:
            shutil.copy(f"{path_directorio_origen}{nombre_archivo}",
                        f"{path_directorio_destino}{filename_destiny}")
        except:
            print("no se copio el archivo")


    def validar_sucursal_seleccionada(self, sucursal):
        logging.info("Validation sucursal selected")
        print(f"validar que la sucursal '{sucursal}' sea seleccionada")
        cont = 0
        assert sucursal in images.SUCURSALES.keys(), f"sucursal '{sucursal}' no existe en a lista"
        #while not self.sucursal_seleccionada(images.img_seleccion_sucursal_12):
        while not self.sucursal_seleccionada(images.SUCURSALES[sucursal]):
            print(f"Try No:{str(cont+1)}")
            print(f"Ingresar numero de sucursal '{sucursal}'")
            self.send_sucursal(sucursal, 0.1)
            self.segundos_de_espera(1)
            cont += 1
            if cont == 5:
                logging.error(f"La sucursal '{sucursal}' no se ha seleccionado, terminando la ejecucion")
                self.stop_pyautogui()


    def login_adm_sge(self, adm_username: str, ip: str, adm_password: str):
        self.sge_connection(adm_username, ip, adm_password)
        time.sleep(2)
        self.send_text("cd automation")
        self.press_enter()
        self.send_text("principaluat02")
        self.press_enter()
        # Menu de sucursales
        time.sleep(1)

    def press_enter(self):
        pa.press('enter')
        time.sleep(1)

    def press_tab(self):
        pa.press('tab')
        time.sleep(1)

    def press_key(self, key_name: str):
        pa.press(key_name)
        time.sleep(1)

    def press_hotkeys(self, hot_key: str):
        hot_key = hot_key.split("+")
        pa.hotkey(hot_key[0].strip(), hot_key[1].strip())

    def send_text(self, my_text: str):
        pa.typewrite(my_text)
        time.sleep(1)

    def segundos_de_espera(self, x_segundos: int):
        time.sleep(x_segundos)

    def validate_adm_sge_connection(self, img_to_validate):
        time.sleep(1)
        s = pa.locateOnScreen(img_to_validate)

        if s is not None:
            # print("Connection Successful!!")
            return True
        else:
            assert False, "Error connection no defined"

    def validar_po_status2(self, img_status_po, nombre_status):
        time.sleep(3)
        print(f"Validating PO Status...{nombre_status}")
        in_screen = pa.locateOnScreen(img_status_po)
        if in_screen != '':
            print(in_screen)
            print(f"PO Status {nombre_status} Correct...")
            message = (f"PO Status {nombre_status} Correct")
            self.take_screenshot(message)
            return True
        if in_screen is not None:
            print(in_screen)
            print(f"PO Status {nombre_status} Correct...")
            message = (f"PO Status {nombre_status} Correct")
            self.take_screenshot(message)
            return True
        if in_screen is None:
            print(in_screen)
            print("PO status not expected...")
            message = ("PO status not expected...")
            self.take_screenshot(message)
            return False

    def leer_archivo_productos(self, archivo_productos):
        with open(archivo_productos, 'r') as f1:
            for line in f1:
                print(line)
                pa.typewrite(line)

    def doubleClick(self, img_doubleClick):
        time.sleep(3)
        img_coordinates = pa.locateCenterOnScreen(img_doubleClick)
        pos_x = img_coordinates[0]
        pos_y = img_coordinates[1]
        nueva_x = pos_x + 10
        pa.doubleClick(nueva_x, pos_y)
        texto_select = str(paste())
        if texto_select != "":
            return texto_select
        if texto_select is not None:
            return texto_select



    def rightClick(self, img_r_Click):
        coordinates_rclick = pa.locateCenterOnScreen(img_r_Click)
        pa.click(coordinates_rclick, button="right")


    def remove_file(self, psc_path_origen, file_name):
        """
        elimina archivo si proporcionas el directorio origen y el nombre del archivo
        :param psc_path_origen:
        :param file_name:
        :return:
        """
        if os.path.exists(psc_path_origen):
            os.remove(f"{psc_path_origen}{file_name}")
        else:
            print("The file does not exist")

    def remove_file2(self, psc_path_origen):
        """
        elimina el archivo proporcionando la ruta completa del archivo
        :param psc_path_origen:
        :return:
        """
        if os.path.exists(psc_path_origen):
            os.remove(psc_path_origen)
        else:
            print("The file does not exist")


    def doubleclick_axis_x(self, img_reference, add_pixels_on_axis_x: int ):
        time.sleep(3)
        """

        :param img_reference:
        :param add_pixels_on_axis_x: pixels to add or reduce from img_reference
        :return:  double click action on new axis x coordinates y regresa el valor del texto seleccionado si existe
        """
        img_coordinates = pa.locateCenterOnScreen(img_reference)
        #print("coordenadas de double click")
        #print(img_coordinates)
        if img_coordinates is not None:
         #   print("coordenadas de double click")
         #   print(img_coordinates)
            pos_x = img_coordinates[0]
            pos_y = img_coordinates[1]
            nueva_x = pos_x + add_pixels_on_axis_x
            pa.doubleClick(nueva_x, pos_y)
            #print(f"double click in new coordinates: {(nueva_x, pos_y)}")
            text_obtained = str(paste())
            return text_obtained


    def validar_imagen_x(self, img_to_validate)->bool:
        time.sleep(5)
        in_screen = pa.locateOnScreen(img_to_validate)
        print(in_screen)
        if in_screen is not None:
            print(in_screen)
            return True

    def validar_imagen_y(self, img_to_validate)->bool:
        time.sleep(5)
        in_screen = pa.locateOnScreen(img_to_validate)
        if in_screen is not None:
        # print(in_screen)
            return True

    def copiar_en_portapapeles(self, texto:str):
        pyperclip.copy(texto)
    def pegar_de_portapapeles(self):
        pyperclip.paste()

    def stop_pyautogui(self):
        raise pa.FailSafeException("Error durante la ejecucion, deteniendo automatizacion")

    def sucursal_seleccionada(self, img_to_validate) -> bool:
        time.sleep(1)
        in_screen = pa.locateOnScreen(img_to_validate)
        #print(in_screen)
        if in_screen is not None:
            print(in_screen)
            print("sucursal seleccionada correctamente")
            return True
        if in_screen is None:
            print(in_screen)
            print("sucursal No fue seleccionada")
            return False
        if in_screen != "":
            print(in_screen)
            print("sucursal seleccionada correctamente")
            return True


    def send_sucursal(self, num_sucursal: str,interval: float):
        pa.typewrite(num_sucursal, interval=interval)

    def activar_cambio_usuario(self):
        pa.typewrite("uu", interval=0.1)




