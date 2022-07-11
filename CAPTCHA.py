# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:31:23 2022

@author: Acer
"""
# Librerias 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from PIL import Image
from io import BytesIO
import time


# opc de navegaciones
options = webdriver.EdgeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\Acer\\Desktop\\data engineer\\msedgedriver.exe'

driver = webdriver.Edge(driver_path)


# Inciar el navegador
driver.get('http://challenge01.root-me.org/programmation/ch8/')

# Buscar la img de la web HTML & save
img = driver.find_element(By.XPATH, '/html/body/img')

img_encontrada = img.location

size = img.size

g_img = driver.get_screenshot_as_png()
img2 = Image.open(BytesIO(g_img))
left = img_encontrada['x']
top = img_encontrada['y']
rigth = img_encontrada['x'] + size['width']
bottom = img_encontrada['y'] + size['height']
img2 = img2.crop((left, top, rigth, bottom))

img2.save('CAPTCHA.png')

# driver.quit()






