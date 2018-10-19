import unittest
import pytest
from selenium import webdriver
import Config
from paginas.PaginaPublicarAviso import PaginaPublicarAviso
import xlrd
import os

class TestPublicarAviso(unittest.TestCase):
    
    #Defino casos de prueba
    
    #Publicar aviso correcto
    def test_publicar_aviso(self):

        wb = xlrd.open_workbook(Config.func_excel_data())
        sh1 = wb.sheet_by_index(2)
        maxfila = sh1.nrows
        i = 1
        while (i < maxfila):
            if Config.func_navegador() == 'Firefox':
                self.driver = webdriver.Firefox(Config.driver_firefox)
            elif Config.func_navegador() == 'Chrome':
                self.driver = webdriver.Chrome(Config.driver_chrome())
            elif Config.func_navegador() == "IExplorer":
                self.driver = webdriver.Ie(Config.driver_iexplorer())
            else:
                self.driver = webdriver.Chrome("")

            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.driver.get(Config.func_url())

            #try:
            rownum = (i)
            rows = sh1.row_values(rownum)
            user = str(rows[0])
            pasw = str(rows[1])
            nombrePuesto = str(rows[2])
            descripcionPuesto = str(rows[3])
            nivelPuesto = str(rows[4])
            areaPuesto = str(rows[5])
            modalidad = str(rows[6])
            salarioMin = str(rows[7])
            salarioMax = str(rows[8])

            #driver = self.driver
            print (" --- Aviso: " + str(i) + " --- ")
            self.assertIn("APTiTUS.com",self.driver.title)
            pagina = PaginaPublicarAviso(self.driver)
            pagina.publicar_aviso(user, pasw, nombrePuesto, descripcionPuesto, nivelPuesto, areaPuesto, modalidad, salarioMin, salarioMax)
            self.assertEqual("¡Felicitaciones!\nTu aviso se ha publicado exitosamente", pagina.get_txt_mensaje_confirmacion())
            print("Test Publicar Aviso OK")
            self.driver.quit()
            i = i + 1

    def test_publicar_aviso_campos_vacios(self):

        wb = xlrd.open_workbook(Config.func_excel_data())
        sh1 = wb.sheet_by_index(2)
        maxfila = sh1.nrows
        i = 1
        while (i < maxfila):
            if Config.func_navegador() == 'Firefox':
                self.driver = webdriver.Firefox()
            elif Config.func_navegador() == 'Chrome':
                self.driver = webdriver.Chrome(Config.driver_chrome())
            elif Config.func_navegador() == "IExplorer":
                self.driver = webdriver.Ie("")
            else:
                self.driver = webdriver.Chrome("")

            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.driver.get(Config.func_url())

            #try:
            rownum = (i)
            rows = sh1.row_values(rownum)
            user = str(rows[0])
            pasw = str(rows[1])
            nombrePuesto = str(rows[2])
            descripcionPuesto = str(rows[3])
            nivelPuesto = str(rows[4])
            areaPuesto = str(rows[5])
            modalidad = str(rows[6])
            salarioMin = str(rows[7])
            salarioMax = str(rows[8])

            #driver = self.driver
            print (" --- Aviso: " + str(i) + " --- ")
            #self.assertIn("APTiTUS.com",self.driver.title)
            pagina = PaginaPublicarAviso(self.driver)
            pagina.publicar_aviso(user, pasw, nombrePuesto, descripcionPuesto, nivelPuesto, areaPuesto, modalidad, salarioMin, salarioMax)
            self.assertEqual("Datos de tu aviso", pagina.get_txt_datos_aviso())
            print("Test Publicar Aviso Campos Vacíos OK")
            self.driver.quit()
            i = i + 1
    