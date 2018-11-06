#from selenium import webdriver
from page_objects import PageObject, page_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from paginas.PaginaLoginEmpresa import PaginaLoginEmpresa
from paginas.PaginaLoginEmpresa import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
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
    clickRequisitos = (By.XPATH, "//DIV[@class='b-section-requirements_title']/self::DIV")
    radioGeneroIndistinto = (By.XPATH, "//SPAN[@class='b-radio_span'][text()='Indistinto']/self::SPAN")
    radioGeneroMasculino = (By.XPATH, "//SPAN[@class='b-radio_span'][text()='Masculino']/self::SPAN")
    radioGeneroFemenino = (By.XPATH, "//SPAN[@class='b-radio_span'][text()='Femenino']/self::SPAN")
    chckGeneroExcluyente = (By.ID, "genderIsExcluding")
    txtEdadMin = (By.ID, "ageMin")
    txtEdadMax = (By.ID, "ageMax")
    chckEdadExcluyente = (By.ID, "ageIsExcluding")
    txtExperienciaMinima = (By.ID, "experienceMin")
    cboArea = (By.ID, "experienceArea")
    chckExperienciaExcluyente = (By.ID, "experienceIsExcluding")
    cboEstudios = (By.ID, "studies.0.gradeId")
    cboAreaEstudios = (By.XPATH, "//DIV[@class='b-select sc-kjoXOD ixTfKM']/self::DIV")
    chckAreaEstudios = (By.XPATH, "//LABEL[@class='b-checkbox_label']/self::LABEL")
    chckEstudiosExcluyente = (By.ID, "studies.0.required")
    cboIdioma = (By.ID, "languages.0.languageId")
    cboNivelIdioma = (By.ID, "languages.0.level")
    chckIdiomaExcluyente = (By.ID, "languages.1.required")
    #txtConocimiento = "programs"
    cboConocimiento = (By.ID, "react-autowhatever-1--item-0")
    chckConocimientoExcluyente = (By.ID, "programsIsExcluding")
    btnContinuar = (By.CSS_SELECTOR, "button.b-btn.sc-gzVnrw.kccGNS")
    btnPublicar = (By.XPATH, "//BUTTON[@type='submit']/../..")
    #cboPregunta = (By.ID, "selTypeQuestions")
    #txtPregunta1 = (By.name, "questions.0.name")
    txtDatosAviso = (By.XPATH, "//H2[@class='b-process-product-type_title b-process-product-type_title--label'][text()='Tipo del aviso']/../../../../..")
    txtMensajeConfirmacion = (By.XPATH, "//P[@class='b-successful-publication_content__paragraph'][text()='¡Felicitaciones!']/../..")

    def link_publicar_aviso(self):
        linkPublicarAvisoElement = self.driver.find_element(*PaginaPublicarAviso.linkPublicarAviso)
        linkPublicarAvisoElement.click()

    def link_publicar(self):
        linkPublicarElement = self.driver.find_element(*PaginaPublicarAviso.linkPublicar)
        linkPublicarElement.click()
    
    def cbo_tipo_aviso(self, tipoAviso):
        cboTipoAvisoElement = self.driver.find_element(*PaginaPublicarAviso.cboTipoAviso)
        select = Select(cboTipoAvisoElement)
        if tipoAviso == 'Premium':
            select.select_by_value("27")
        if tipoAviso == 'Destacado':
            select.select_by_value("28")
        else:
            select.select_by_value("29")       
    
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
    
    def set_click_requisitos(self):
        clickRequisitosElement = self.driver.find_element(*PaginaPublicarAviso.clickRequisitos)
        self.driver.execute_script("arguments[0].click();", clickRequisitosElement)
    
    def set_radio_genero(self, genero):
        radioGeneroIndistintoElement = self.driver.find_element(*PaginaPublicarAviso.radioGeneroIndistinto)
        radioGeneroMasculinoElement = self.driver.find_element(*PaginaPublicarAviso.radioGeneroMasculino)
        radioGeneroFemeninoElement = self.driver.find_element(*PaginaPublicarAviso.radioGeneroFemenino)
        if genero == "I":
            self.driver.execute_script("arguments[0].click();", radioGeneroIndistintoElement)
        if genero == "M":
            self.driver.execute_script("arguments[0].click();", radioGeneroMasculinoElement)
        else:
            self.driver.execute_script("arguments[0].click();", radioGeneroFemeninoElement)

    def set_chck_genero_excluyente(self, generoExcluyente):
        chckGeneroExcluyenteElement = self.driver.find_element(*PaginaPublicarAviso.chckGeneroExcluyente)
        if generoExcluyente == "Si":
            self.driver.execute_script("arguments[0].click();", chckGeneroExcluyenteElement)

    def set_txt_edad_minima(self, edadMin):
        edadMinElement = self.driver.find_element(*PaginaPublicarAviso.txtEdadMin)
        edadMinElement.send_keys(edadMin)
    
    def set_txt_edad_maxima(self, edadMax):
        edadMaxElement = self.driver.find_element(*PaginaPublicarAviso.txtEdadMax)
        edadMaxElement.send_keys(edadMax)

    def set_txt_experiencia_min(self, experienciaMinima):
        txtExperienciaMinimaElement = self.driver.find_element(*PaginaPublicarAviso.txtExperienciaMinima)
        txtExperienciaMinimaElement.clear()
        txtExperienciaMinimaElement.send_keys(experienciaMinima)
    
    def set_cbo_area(self, area):
        cboAreaElement = self.driver.find_element(*PaginaPublicarAviso.cboArea)
        cboAreaElement.send_keys(area)
    
    def set_cbo_estudios(self, estudio):
        cboEstudiosElement = self.driver.find_element(*PaginaPublicarAviso.cboEstudios)
        cboEstudiosElement.send_keys(estudio)
    
    def set_cbo_area_estudios(self, areaEstudio):
        cboAreaEstudiosElement = self.driver.find_element(*PaginaPublicarAviso.cboAreaEstudios)
        chckAreaEstudiosElement = self.driver.find_element(*PaginaPublicarAviso.chckAreaEstudios)
        cboAreaEstudiosElement.click()
        chckAreaEstudiosElement.send_keys(areaEstudio)
    
    def set_cbo_idioma(self, idioma):
        cboIdiomaElement = self.driver.find_element(*PaginaPublicarAviso.cboIdioma)
        cboIdiomaElement.send_keys(idioma)
    
    def set_cbo_nivel_idioma(self, nivelIdioma):
        cboNivelIdiomaElement = self.driver.find_element(*PaginaPublicarAviso.cboNivelIdioma)
        cboNivelIdiomaElement.send_keys(nivelIdioma)

    def set_txt_conocimiento(self, conocimiento):
        txtConocimientoElement = self.driver.find_element_by_name("programs")
        txtConocimientoElement.send_keys(conocimiento)
        cboConocimientoElement = self.driver.find_element(*PaginaPublicarAviso.cboConocimiento)
        time.sleep(1)
        cboConocimientoElement.click()
        
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
    
    def publicar_aviso(self, usuario, password, tipoAviso, nombrePuesto, descripcionPuesto, areaPuesto, nivelPuesto, modalidad, salarioMinimo, salarioMaximo, genero,
                        generoExcluyente, edadMin, edadMax, experienciaMinima, area, estudio, areaEstudio, idioma, nivelIdioma, conocimiento):
        login = PaginaLoginEmpresa(self.driver)
        login.link_soy_una_empresa()
        login.link_ingresa()
        login.set_txtUser(usuario)
        login.set_txtPassword(password)
        login.btn_ingresar()
        time.sleep(5)
        self.link_publicar_aviso()
        self.link_publicar()
        self.cbo_tipo_aviso(tipoAviso)
        self.set_txt_nombre_puesto(nombrePuesto)
        self.set_txt_descripcion_puesto(descripcionPuesto)
        self.set_cbo_area_puesto(areaPuesto)
        self.set_cbo_nivel_puesto(nivelPuesto)
        self.set_cbo_modalidad(modalidad)
        #self.set_cbo_nombre_empresa()
        self.set_txt_salario_min(salarioMinimo)
        self.set_txt_salario_max(salarioMaximo)
        #self.set_click_requisitos()
        time.sleep(1)
        self.set_radio_genero(genero)
        time.sleep(1)
        self.set_chck_genero_excluyente(generoExcluyente)
        self.set_txt_edad_minima(edadMin)
        self.set_txt_edad_maxima(edadMax)
        self.set_txt_experiencia_min(experienciaMinima)
        self.set_cbo_area(area)
        #self.set_cbo_estudios(estudio)
        #self.set_cbo_area_estudios(areaEstudio)
        self.set_cbo_idioma(idioma)
        self.set_cbo_nivel_idioma(nivelIdioma)
        self.set_txt_conocimiento(conocimiento)
        time.sleep(2)
        self.set_btn_continuar()
        time.sleep(5)
        self.set_btn_publicar()
        time.sleep(5)
        #login.click_header_usuario()
        #login.link_cerrar_sesion()