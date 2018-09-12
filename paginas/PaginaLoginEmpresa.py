from page_objects import PageObject, page_element
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__ (self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30 

class PaginaLoginEmpresa(BasePage):

    #Declarando elementos de la página
    linkSoyUnaEmpresa = (By.LINK_TEXT,"Soy una Empresa")
    linkIngresa = (By.LINK_TEXT,"Ingresa")
    txtUser = (By.ID, "txtUser")
    txtPassword = (By.ID, "txtPasswordLogin")
    btnIngresar = (By.ID, "frmUserLogIn")
    txtEmpresa = (By.LINK_TEXT, "Empresas")
    #clickHeaderUsuario = (By.CSS_SELECTOR, "div.nav_session_header.js-session-header")
    clickHeaderUsuario = (By.XPATH, "//DIV[@class='nav_session_header js-session-header']/self::DIV")
    linkCerrarSesion = (By.LINK_TEXT, "Cerrar sesión")
    txtAccedeCuenta = (By.XPATH, "//DIV[@class='g-modal_title'][text()='Accede a tu cuenta']/self::DIV")

    
    def link_soy_una_empresa(self):
        linkSoyUnaEmpresaElement= self.driver.find_element(*PaginaLoginEmpresa.linkSoyUnaEmpresa)
        linkSoyUnaEmpresaElement.click()

    def link_ingresa(self):
        linkIngresaElement= self.driver.find_element(*PaginaLoginEmpresa.linkIngresa)
        linkIngresaElement.click()

    def set_txtUser(self, usuario):
        txtUserElement= self.driver.find_element(*PaginaLoginEmpresa.txtUser)
        txtUserElement.send_keys(usuario)
    
    def set_txtPassword(self, password):
        txtPasswordElement= self.driver.find_element(*PaginaLoginEmpresa.txtPassword)
        txtPasswordElement.send_keys(password)

    def btn_ingresar(self):
        btnIngresarElement = self.driver.find_element(*PaginaLoginEmpresa.btnIngresar)
        btnIngresarElement.submit()

    def click_header_usuario(self):
        clickHeaderUsuarioElement = self.driver.find_element(*PaginaLoginEmpresa.clickHeaderUsuario)
        clickHeaderUsuarioElement.click()
    
    def link_cerrar_sesion(self):
        linkCerrarSesionElement = self.driver.find_element(*PaginaLoginEmpresa.linkCerrarSesion)
        linkCerrarSesionElement.click()

    def txt_accede_cuenta(self):
        txtAccedeCuentaElement = self.driver.find_element(*PaginaLoginEmpresa.txtAccedeCuenta)
        return txtAccedeCuentaElement.text
    
    def txt_empresa(self):
        txtEmpresaElement = self.driver.find_element(*PaginaLoginEmpresa.txtEmpresa)
        return txtEmpresaElement.text

    def login(self, usuario, password):
        if (usuario is "" or usuario is None)  or (password is "" or password is None):
            self.link_soy_una_empresa()
            self.link_ingresa()
            self.set_txtUser(usuario)
            self.set_txtPassword(password)
            self.btn_ingresar()           
        else:
            self.link_soy_una_empresa()
            self.link_ingresa()
            self.set_txtUser(usuario)
            self.set_txtPassword(password)
            self.btn_ingresar()
            self.driver.implicitly_wait(30)
            self.click_header_usuario()
            self.link_cerrar_sesion()