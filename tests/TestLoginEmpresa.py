import unittest
import pytest
from selenium import webdriver
import Config
from paginas.PaginaLoginEmpresa import PaginaLoginEmpresa
import xlrd
import os

class TestLoginEmpresa(unittest.TestCase):
    
    #Defino casos de prueba
    
    #Login empresa correcto
    def test_login_empresa(self):

        wb = xlrd.open_workbook(Config.func_excel_data())
        sh1 = wb.sheet_by_index(0)
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
            #driver = self.driver
            print (" --- Login: " + str(i) + " --- ")
            self.assertIn("APTiTUS.com",self.driver.title)
            pagina = PaginaLoginEmpresa(self.driver)
            pagina.login(user, pasw)
            self.assertEqual("Empresas", pagina.txt_empresa())
            print("Test Login Empresa OK")
            self.driver.quit()
            i = i + 1

            """self.driver = webdriver.Chrome(Config.driver_chrome())
            self.driver.maximize_window()
            self.driver.get(Config.func_url())
            self.assertIn("APTiTUS.com",self.driver.title)
            pagina = PaginaLoginEmpresa(self.driver)
            pagina.login("cempresa1@ecodigital.pe","123456abc")
            self.assertEqual("Empresa", pagina.txt_empresa())
            print("Test Login Empresa OK")
            self.driver.quit()"""
        

    #Login empresa incorrecto con usuario y/o password vacíos
    def test_login_empresa_incorrecto_campos_vacios(self):

        wb = xlrd.open_workbook(Config.func_excel_data())
        sh1 = wb.sheet_by_index(1)
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
            #driver = self.driver
            print (" --- Login: " + str(i) + " --- ")
            self.assertIn("APTiTUS.com",self.driver.title)
            pagina = PaginaLoginEmpresa(self.driver)
            pagina.login(user, pasw)
            self.assertEqual("Accede a tu cuenta",pagina.txt_accede_cuenta())
            print("Test Login Empresa Campos Vacíos OK")
            self.driver.quit()
            i = i + 1
        '''
        self.driver = webdriver.Chrome(Config.driver_chrome())
        self.driver.maximize_window()
        self.driver.get(Config.func_url())
        self.assertIn("APTiTUS.com",self.driver.title)
        pagina = PaginaLoginEmpresa(self.driver)
        pagina.login("","123456abc")
        self.assertEqual("Accede a tu cuenta",pagina.txt_accede_cuenta())
        print("Test Login Empresa Campos Vacíos OK")
        self.driver.quit()'''


