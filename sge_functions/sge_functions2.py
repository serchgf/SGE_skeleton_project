import logging
import random
import base64
from allure_commons.types import AttachmentType
import allure
import pyperclip
from PIL import Image as im
from Config.config import txt_files_path
from Config.config import login_data

from Config.config import files
from Config.config import images

import os
import pyautogui as pa
import subprocess
import time
import datetime
import shutil
from pyperclip import paste

class sge_functions2:
    img_pantalla_inicial = images.img_pantalla_inicial
    img_error_connection = images.img_error_connection
    img_inicio_orden_de_compra = images.img_inicio_orden_de_compra

    #############
    img_promociones = images.img_promociones
    img_promociones2 = images.img_promociones2
    img_atraso = images.img_error_atraso_importante
    error_cedi_preferente = images.img_error_cedi_preferente
    #############

    close_as = ""

    def create_report_directory(self):
        logging.info("Creating Report Directory")
        main_report_dir = 'Reports/SGE_Test_report_' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M/")
        """main_report_dir = 'images_report/SGE_PO_Test_report ' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S/")"""
        return main_report_dir

    def sge_connection(self, username, ip, password):
        logging.info("Trying to Connect with SGE")
        try:
            connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)
            subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            time.sleep(3)
        except:
            print("Connection Failed...\nCheck your credentials access...")

    def validate_sge_connection(self):
        logging.info("Validate SGE connection")
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

    def take_screenshot(self, message):
        logging.info("Taking screenshot")
        print("taking screenshot " + message)
        img_name = f"my_screenshot.png"
        pa.screenshot(f"Screenshots/{img_name}")


        pa.screenshot(f"{files.screenshot_folder}{images.img_allure_screenshot_name}")

        #print("dhfosidhfsihdfpshfdpshfpsi")
        #print(os.getcwd()+"/Screenshots/my_allure_screenshot.png")
        rr = os.getcwd()+"\\Screenshots\\my_allure_screenshot.png"
        cadena = "".join(rr)
        with open(cadena, "rb")as img_file:
            f = img_file.read()
            #b = bytearray(f)
        allure.attach(f,name="para_Allure_report", attachment_type=AttachmentType.PNG)


    def close_sge_session(self, close_as= None):
        logging.info("Close SGE connection")
        pa.hotkey('alt', 'f4')
        time.sleep(1)
        pa.press('enter')

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

    def fecha_yyyymmdd(self):
        from datetime import datetime
        print(datetime.today().strftime('%Y%m%d'))
        return datetime.today().strftime('%Y%m%d')

    def error_screenshot(self):
        message = "connection_error"
        self.take_screenshot(message)

    def terminate_sge_session(self):
        logging.info("Terminate SGE session")
        print("Test finished...")
        self.close_sge_session(self.close_as)
        print("Session terminated")

    def move_to_report_dir(self, img_to_move, path_to_move):
        logging.info("Move files/images to Report Directory")
        try:
            shutil.move(f"Screenshots/my_screenshot.png", f"{path_to_move}/{img_to_move}")
            file_source = files.directory_tmp_file
            file_destination = path_to_move
            get_files = os.listdir(file_source)
            for f in get_files:
                try:
                    shutil.move(file_source + f, file_destination + f)
                except:
                 print("Error, INV file no Generated")
        except:
            pass

        return f"images_report/{img_to_move}"

    def promociones_y_atrasos(self):
        logging.info("Looking for offers and payments delays")
        gdl = pa.locateOnScreen(self.error_cedi_preferente)
        atraso = pa.locateOnScreen(self.img_atraso)
        p2 = pa.locateOnScreen(self.img_promociones2)
        p = pa.locateOnScreen(self.img_promociones)
        if atraso is not None or p is not None or p2 is not None or gdl is not None:
            return True
        else:
            return False

    def sugerencia_CEDI(self):
        time.sleep(2)
        gdl = pa.locateOnScreen(self.error_cedi_preferente)
        if gdl is not None:
            pa.press('s')

    def press_enter(self):
        logging.info("Press Enter")
        pa.press('enter')
        time.sleep(1)

    def press_tab(self):
        logging.info("Press Tab")
        pa.press('tab')
        time.sleep(1)

    def press_key(self, key_name: str):
        logging.info(f"Press key: {key_name}")
        pa.press(key_name)
        time.sleep(1)

    def press_del(self):
        logging.info(f"Press key: del")
        pa.press("del")

    def clean_field(self):
        for i in range(20):
            self.press_del()

    def press_hotkeys(self, hot_key: str):
        logging.info(f"Press hotkey: {hot_key}")
        hot_key = hot_key.split("+")
        pa.hotkey(hot_key[0].strip(), hot_key[1].strip())

    def send_text(self, my_text: str):
        logging.info(f"Write: {my_text}")
        pa.typewrite(my_text)
        time.sleep(1)

    def segundos_de_espera(self, x_segundos: int):
        logging.info(f"Waiting {x_segundos} seconds to continue")
        time.sleep(x_segundos)

    def validate_adm_sge_connection(self, img_to_validate):
        logging.info("Validate SGE connection")
        time.sleep(2)
        s = pa.locateOnScreen(img_to_validate)
        print("-----------------------------------")
        print(s)
        print("-----------------------------------")
        if s is not None:
            # print("Connection Successful!!")
            return True
        else:
            message = "SGE HomePage not found"
            self.take_screenshot(message)
            return False

    def validating_invoice(self):
        logging.info("Validation Invoice creation")
        time.sleep(2)
        coord_xy = pa.locateOnScreen(images.img_invoice_created_correctly)

        if coord_xy == None or coord_xy == "":
            print("An error has Occurred during Invoice creation")
            message = "Error_during_invoice_creation"
            self.take_screenshot(message)
            return False
        else:
            print("Invoice created succesfully")
            message = "Invoice created succesfully"
            self.take_screenshot(message)
            return True

    # def validating_invoice_20(self):
    #     logging.info("Validation Invoice creation")
    #     coord_xy = pa.locateOnScreen(images.img_invoice_created_correctly_20)
    #
    #     if coord_xy == None or coord_xy == "":
    #         print("An error has Occurred during Invoice creation")
    #         message = "Error_during_invoice_creation"
    #         self.take_screenshot(message)
    #         return False
    #     else:
    #         print("Invoice created succesfully")
    #         message = "Invoice created succesfully"
    #         self.take_screenshot(message)
    #         return True
    #
    # def validating_invoice_50(self):
    #     logging.info("Validation Invoice creation")
    #     coord_xy = pa.locateOnScreen(images.img_invoice_created_correctly_50)
    #
    #     if coord_xy == None or coord_xy == "":
    #         print("An error has Occurred during Invoice creation")
    #         message = "Error_during_invoice_creation"
    #         self.take_screenshot(message)
    #         return False
    #     else:
    #         print("Invoice created succesfully")
    #         message = "Invoice created succesfully"
    #         self.take_screenshot(message)
    #         return True


    def leer_archivo_productos(self, archivo_productos):
        logging.info("Leer Archivo")
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
        if texto_select != "" or texto_select is not None:
            return texto_select

    def rightClick(self, img_r_Click):
        coordinates_rclick = pa.locateCenterOnScreen(img_r_Click)
        pa.click(coordinates_rclick, button="right")

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

    def sucursal_seleccionada(self, img_to_validate) -> bool:
        time.sleep(1)
        in_screen = pa.locateOnScreen(img_to_validate)
        print(in_screen)
        if in_screen is not None:
            print(in_screen)
            return True
        if in_screen is None:
            print(in_screen)
            return False
        if in_screen != "":
            return True

    def stop_pyautogui(self):
        raise pa.FailSafeException("Error durante la ejecucion, deteniendo automatizacion")

    def validate_image_x(self, img_to_validate) -> bool:
        time.sleep(2)
        in_screen = pa.locateOnScreen(img_to_validate)
        print(in_screen)
        if in_screen is not None:
            print(in_screen)
            return True
        if in_screen is None:
            print(in_screen)
            return False
        if in_screen != "":
            return True

    # def validar_sucursal_12_seleccionada(self):
    #     print("validar que la sucursal 12 sea seleccionada")
    #     cont = 0
    #     #while not self.sucursal_seleccionada(images.img_seleccion_sucursal_12):
    #     while not self.sucursal_seleccionada(images.img_sucursal_12_selec_mods):
    #         print(f"Try No:{str(cont+1)}")
    #         print("5 Ingresar numero de sucursal ")
    #         self.send_sucursal("12", 0.1)
    #         self.segundos_de_espera(1)
    #         cont += 1
    #         if cont == 5:
    #             logging.error("La sucursal no se ha seleccionado, terminando la ejecucion")
    #             self.stop_pyautogui()

    def send_sucursal(self, num_sucursal: str,interval: float):
        pa.typewrite(num_sucursal, interval=interval)

    def activar_cambio_usuario(self):
        pa.typewrite("uu", interval=0.1)

    def activar_menu_mods(self):
        pa.typewrite("mm", interval=0.1)

    def flecha_abajo(self):
        pa.hotkey("ctrl", "down")

    def flecha_arriba(self):
        pa.hotkey("ctrl", "up")

    def doubleclick_axis_xy(self, img_reference, add_pixels_on_axis_x: int, add_pixels_on_axis_y: int):
        time.sleep(3)
        """
        :param img_reference:
        :param add_pixels_on_axis_x: pixels to add or reduce from img_reference
        :return: double click action on new axis x coordinates y regresa el valor del texto seleccionado si existe
        """
        img_coordinates = pa.locateCenterOnScreen(img_reference)
        # print("coordenadas de double click")
        # print(img_coordinates)
        if img_coordinates is not None:
            # print("coordenadas de double click")
            # print(img_coordinates)
            pos_x = img_coordinates[0]
            pos_y = img_coordinates[1]
            nueva_x = pos_x + add_pixels_on_axis_x
            nueva_y = pos_y + add_pixels_on_axis_y
            pa.doubleClick(nueva_x, nueva_y)
            # print(f"double click in new coordinates: {(nueva_x, pos_y)}")
            text_obtained = str(paste())
            return text_obtained

    def doubleclick_axis_y(self, img_reference, add_pixels_on_axis_y: int ):
        time.sleep(3)
        """
        :param img_reference:
        :param add_pixels_on_axis_x: pixels to add or reduce from img_reference
        :return: double click action on new axis x coordinates y regresa el valor del texto seleccionado si existe
        """
        img_coordinates = pa.locateCenterOnScreen(img_reference)
        #print("coordenadas de double click")
        #print(img_coordinates)
        if img_coordinates is not None:

            # print("coordenadas de double click")
            # print(img_coordinates)
            pos_x = img_coordinates[0]
            pos_y = img_coordinates[1]
            nueva_y = pos_y + add_pixels_on_axis_y
            pa.doubleClick(pos_x, nueva_y)
            #print(f"double click in new coordinates: {(nueva_x, pos_y)}")
            text_obtained = str(paste())
            return text_obtained