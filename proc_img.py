# -*- coding: utf-8 -*-
"""
Creaed on Fri Jul  8 21:48:01 2022

@author: Acer
"""

""" Obtengo texto de la imagen con vision de G-cloud"""

from google.cloud import vision
import io
from CAPTCHA import *
import re

# implemento un modelo pre entrenado de vision con G-cloud
client = vision.ImageAnnotatorClient()

with io.open('C:/Users/Acer/Desktop/data engineer/CAPTCHA.png', 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

    print('limites: {}'.format(','.join(vertices)))

if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))

myword = texts[0].description

patron = '[\W+]'

regex = re.compile(patron)

resultado = regex.sub('', myword)

# Tomo caracteres y los agrego a la utomatizacion
WebDriverWait(driver, 2)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input'))).click()

WebDriverWait(driver, 2)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input'))).send_keys(resultado)


print('\n CAPTCHA a utilizar: "{}"'.format(resultado))


