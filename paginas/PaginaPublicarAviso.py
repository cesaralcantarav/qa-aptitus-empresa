#from selenium import webdriver
from page_objects import PageObject, page_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from paginas.PaginaLoginEmpresa import PaginaLoginEmpresa
from paginas.PaginaLoginEmpresa import BasePage
from selenium.webdriver.support.ui import Select
import time

class PaginaPublicarAviso(BasePage):

    linkPublicarAviso = (By.LINK_TEXT,"Publica un aviso")
    #linkPublicarAviso = (By.XPATH, "//A[@href='/empresa/publica-aviso'][text()='Publica un aviso']/../../..")
    linkPublicar = (By.CSS_SELECTOR,"a.btn.btn_notice_publish")
    cboTipoAviso = (By.ID, "productId")
    txtNombrePuesto = (By.ID, "title")
    txtDescripcionPuesto = (By.CSS_SELECTOR, "div.notranslate.public-DraftEditor-content")
    #txtEmpresa = (By.LINK_TEXT, "Empresas")
    cboNivelPuesto = (By.ID,"levelId")
    cboAreaPuesto = (By.ID, "areaId")
    cboModalidad = (By.ID, "contractId")
    cboNombreEmpresa = (By.ID, "companyDisplayType")
    txtSalarioMin = (By.ID, "salaryMin")
    txtSalarioMax = (By.ID, "salaryMax")
    btnContinuar = (By.CSS_SELECTOR, "button.b-btn.sc-gzVnrw.kccGNS")
    btnPublicar = (By.XPATH, "//BUTTON[@type='submit']/../..")
    #cboPregunta = (By.ID, "selTypeQuestions")
    #txtPregunta1 = (By.name, "questions.0.name")
    txtDatosAviso = (By.XPATH, "//DIV[@class='b-process-header_title sc-htoDjs mZUUH'][text()='Datos de tu aviso']/../../..")
    txtMensajeConfirmacion = (By.XPATH, "//P[@class='b-successful-publication_content__paragraph'][text()='¡Felicitaciones!']/../..")


    def link_publicar_aviso(self):
        linkPublicarAvisoElement = self.driver.find_element(*PaginaPublicarAviso.linkPublicarAviso)
        linkPublicarAvisoElement.click()

    def link_publicar(self):
        linkPublicarElement = self.driver.find_element(*PaginaPublicarAviso.linkPublicar)
        linkPublicarElement.click()
    
    def cbo_tipo_aviso(self):
        cboTipoAvisoElement = self.driver.find_element(*PaginaPublicarAviso.cboTipoAviso)
        select = Select(cboTipoAvisoElement)
        select.select_by_value("27")
    
    def set_txt_nombre_puesto(self, nombrePuesto):
        txtNombrePuestoElement = self.driver.find_element(*PaginaPublicarAviso.txtNombrePuesto)
        txtNombrePuestoElement.send_keys(nombrePuesto)
    
    def set_txt_descripcion_puesto(self, descripcionPuesto):
        txtDescripcionPuestoElement = self.driver.find_element(*PaginaPublicarAviso.txtDescripcionPuesto)
        txtDescripcionPuestoElement.send_keys(descripcionPuesto)

    def set_cbo_nivel_puesto(self, nivelPuesto):
        cboNivelPuestoElement = self.driver.find_element(*PaginaPublicarAviso.cboNivelPuesto)
        cboNivelPuestoElement.send_keys(nivelPuesto)

    def set_cbo_area_puesto(self, areaPuesto):
        cboAreaPuestoElement = self.driver.find_element(*PaginaPublicarAviso.cboAreaPuesto)
        cboAreaPuestoElement.send_keys(areaPuesto)

    def set_cbo_modalidad(self, modalidad):
        cboModalidadElement = self.driver.find_element(*PaginaPublicarAviso.cboModalidad)
        cboModalidadElement.send_keys(modalidad)

    def set_cbo_nombre_empresa(self):
        cboNombreEmpresaElement = self.driver.find_element(*PaginaPublicarAviso.cboNombreEmpresa)
        select = Select(cboNombreEmpresaElement)
        select.select_by_value("hidden")

    def set_txt_salario_min(self, salarioMinimo):
        txtSalarioMinElement = self.driver.find_element(*PaginaPublicarAviso.txtSalarioMin)
        txtSalarioMinElement.send_keys(salarioMinimo)
    
    def set_txt_salario_max(self, salarioMaximo):
        txtSalarioMaxElement = self.driver.find_element(*PaginaPublicarAviso.txtSalarioMax)
        txtSalarioMaxElement.send_keys(salarioMaximo)
    
    def set_btn_continuar(self):
        btnContinuarElement = self.driver.find_element(*PaginaPublicarAviso.btnContinuar)
        #btnContinuarElement.click()
        self.driver.execute_script("arguments[0].click();", btnContinuarElement)

    def set_btn_publicar(self):
        btnPublicarElement = self.driver.find_element(*PaginaPublicarAviso.btnPublicar)
        btnPublicarElement.submit()

    def get_txt_datos_aviso(self):
        txtDatosAvisoElement = self.driver.find_element(*PaginaPublicarAviso.txtDatosAviso)
        txtDatosAvisoElement.text

    def get_txt_mensaje_confirmacion(self):
        txtMensajeConfirmacionElement = self.driver.find_element(*PaginaPublicarAviso.txtMensajeConfirmacion)
        return txtMensajeConfirmacionElement.text
    

    def publicar_aviso(self, usuario, password, nombrePuesto, descripcionPuesto, areaPuesto, nivelPuesto, modalidad, salarioMinimo, salarioMaximo):
        login = PaginaLoginEmpresa(self.driver)
        login.link_soy_una_empresa()
        login.link_ingresa()
        login.set_txtUser(usuario)
        login.set_txtPassword(password)
        login.btn_ingresar()
        time.sleep(5)
        self.link_publicar_aviso()
        self.link_publicar()
        self.cbo_tipo_aviso()
        self.set_txt_nombre_puesto(nombrePuesto)
        self.set_txt_descripcion_puesto(descripcionPuesto)
        self.set_cbo_area_puesto(areaPuesto)
        self.set_cbo_nivel_puesto(nivelPuesto)
        self.set_cbo_modalidad(modalidad)
        #self.set_cbo_nombre_empresa()
        self.set_txt_salario_min(salarioMinimo)
        self.set_txt_salario_max(salarioMaximo)
        self.set_btn_continuar()
        time.sleep(5)
        self.set_btn_publicar()
        time.sleep(5)
        #login.click_header_usuario()
        #login.link_cerrar_sesion()