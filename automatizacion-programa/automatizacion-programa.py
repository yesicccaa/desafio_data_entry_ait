import pyautogui
import time
import os
import keyboard

# Abrir la calculadora
os.system('start "" "C:\\Windows\\System32\\mspaint.exe"')

# Espera a que se abra Paint
time.sleep(3)

pyautogui.hotkey('winleft', 'up')  # Simula "Windows + flecha arriba" para asegurarse que la ventana esté maximizada

#Escribir texto
pyautogui.click(x=357, y=68) #Clic en el boton para escribir

pyautogui.click(x=384, y=414) #Click en la zona donde vamos a escribir


pyautogui.write('Holaaa! no me anda la calculadora!') #Texto a ingresar
pyautogui.click(x=530, y=300) #Para cerrar cuadro de texto
time.sleep(1)
#Dibujar estrella
pyautogui.click(x=493, y=104, duration=0.3) #click en estrella
time.sleep(2)
time.sleep(2)

pyautogui.moveTo(300, 300, duration=0.5) # Mover el mouse a la posición inicial
pyautogui.mouseDown() #mantener presionada el mouse
pyautogui.moveRel(250, 250, duration=0.6)   # Mover 100 píxeles hacia abajo
pyautogui.mouseUp()
pyautogui.click(x=808, y=208) #Finalizar dibujo

# CERRAR Y GUARDAR ARCHIVO
pyautogui.hotkey('alt', 'f4') #Cerrar Paint con Alt + F4
time.sleep(1) 

pyautogui.write('dibujo_estrella') # Escribir el nombre del archivo
time.sleep(0.5)

pyautogui.press('enter') #Confirmar con Enter para guardar
time.sleep(1)

#Si se abre una ventana de confirmación de sobrescribir, seleccionar que si
pyautogui.press('enter') 
pyautogui.press('left')
time.sleep(1)
pyautogui.press('enter') 




'''
Utilizar esta funcion para guiarse con las coordenadas
  Requiere instalar 'keyboard' con: pip install keyboard

print("Coloca el mouse en la posición deseada y presiona 'p' para capturar las coordenadas.")

Esperar a que se presione la tecla 'p'
keyboard.wait('p')

 Obtener la posición actual del mouse
x, y = pyautogui.position()
print(f"Coordenadas capturadas: X = {x}, Y = {y}")

'''