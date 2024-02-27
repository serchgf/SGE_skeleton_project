"""
pip install pytest-html
install pip install ansi2html
pip install ddt
"""
import os


class login_data:
    # uat02
    ambiente = ""
    programas = ""
    username = ""
    password = ""
    ip = ""

    # usuario Rol de almacen, Alta y Permisos
    usuario_almacen_alta_y_permisos = ""
    usuario_almacen_alta_y_permisos_0 = ""
    # usuario Rol de comprador, Alta y relacion a linea de articulos
    usuario_de_compras = ""
    usuario_de_compras_sr_pro_man = ""

    adm_username =''
    adm_password = ""
    usuario_adm_grecia = ""


class data_sftp_connection:
    sftp_hostname = ""
    sftp_username = ""
    sftp_password = ""
    sftp_port = ""


class csv_files_path:
    main_dir = "Config/TestDataSet/"
    pass


class txt_files_path:
    txt_datos_productos_po = "Config/TestDataSet/datos_productos_po.txt"


class files:
    directory_tmp_file = "tmp_file/"
    screenshot_folder = "screenshots/"
    config_dataset_folder = "Config/TestDataSet/"
    mtc_asge_001_json = "Config/TestDataSet/mtc_asge_001.json"
    valid_inv_confirmed_po_file = "valid_inv_confirmed_po/"


class images:
    """images location"""
    img_allure_screenshot_name = "my_allure_screenshot.png"
    ROOT = os.path.abspath(os.path.join(".", os.pardir))
    img_sge_adm_pantalla_inicial = f"image_files/sge_adm_pantalla_inicial.png"
    img_header_orden_de_compra = "image_files/header_orden_de_compra.png"
    img_pantalla_inicial = f"image_files/pantallaInicial.png"
    img_error_connection = f"image_files/errorConexion2.png"
    img_error_atraso_importante = f"image_files/Error atraso importante.png"
    img_error_gdl = f"image_files/error Guadalajara.png"
    img_invoice_created_correctly = f"image_files/folioGeneradoValidacion.png"
    img_rclick_carga_masiva = f"image_files/rclick_carga_masiva.png"
    img_rclick_buscar_factura_tc4 = f"image_files/rclick_buscar_factura_tc4.png"
    img_rclick_num_pedimento = "image_files/rclick_num_pedimento.png"
    img_promociones = f"image_files/promociones.png"
    img_promociones2 = f"image_files/promociones2.png"
    img_inicio_orden_de_compra = "image_files/inicioOrdenCompra.png"
    img_consulta_orden_de_compra = "image_files/consulta_oc.png"
    img_confirmacion_colocada = "image_files/confirmacionColocada.png"
    img_status_confirmada_por_proveedor = "image_files/status_confirmada.png"
    img_seleccion_sucursal_20 = "image_files/sucursal_20.png"

    SUCURSALES = {
        '1': 'image_files/sucursal_1.png', '2': 'image_files/sucursal_2.png', '3': 'image_files/sucursal_3.png',
        '4': 'image_files/sucursal_4.png', '5': 'image_files/sucursal_5.png', '6': 'image_files/sucursal_6.png',
        '7': 'image_files/sucursal_7.png', '8': 'image_files/sucursal_8.png', '9': 'image_files/sucursal_9.png',
        '10': 'image_files/sucursal_10.png', '11': 'image_files/sucursal_11.png', '12': 'image_files/sucursal_12.png',
        '13': 'image_files/sucursal_13.png', '14': 'image_files/sucursal_14.png', '15': 'image_files/sucursal_15.png',
        '16': 'image_files/sucursal_16.png', '17': 'image_files/sucursal_17.png', '18': 'image_files/sucursal_18.png',
        '19': 'image_files/sucursal_19.png', '20': 'image_files/sucursal_20.png', '21': 'image_files/sucursal_21.png',
        '22': 'image_files/sucursal_22.png', '23': 'image_files/sucursal_23.png', '24': 'image_files/sucursal_24.png',
        '25': 'image_files/sucursal_25.png', '26': 'image_files/sucursal_26.png', '27': 'image_files/sucursal_27.png',
        '28': 'image_files/sucursal_28.png', '29': 'image_files/sucursal_29.png', '30': 'image_files/sucursal_30.png',
        '31': 'image_files/sucursal_31.png', '32': 'image_files/sucursal_32.png', '33': 'image_files/sucursal_33.png',
        '34': 'image_files/sucursal_34.png', '35': 'image_files/sucursal_35.png', '36': 'image_files/sucursal_36.png',
        '37': 'image_files/sucursal_37.png', '38': 'image_files/sucursal_38.png', '39': 'image_files/sucursal_39.png',
        '40': 'image_files/sucursal_40.png', '41': 'image_files/sucursal_41.png', '42': 'image_files/sucursal_42.png',
        '43': 'image_files/sucursal_43.png', '44': 'image_files/sucursal_44.png', '45': 'image_files/sucursal_45.png',
        '46': 'image_files/sucursal_46.png', '47': 'image_files/sucursal_47.png'}

    #------------------------------INTERNACIONAL JOB SCP
    img_status_job_psc_internacional_ok = "image_files/status_job_psc_internacional_ok.png"


class image_root:
    ROOT = os.path.abspath(os.path.join(".", os.pardir))
