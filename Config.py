import os

# Navegador para las pruebas
def func_navegador():
    nav = 'Chrome'      # Firefox,Chrome,IExplorer
    return nav

# Ingresar la url
def func_url():
    url = "https://pre4b.aptitus.com/"  # cambiar si es necesario
    return url

# =================================  Data Excel ================================================
def func_excel_data():
    d = os.getcwd()
    ruta = d + "/data/data.xls"
    return ruta

# ================================ Rutas de Drivers =============================================

def driver_chrome():
    dr = os.getcwd()
    rutad = dr + "/drivers/chromedriver.exe"
    return rutad