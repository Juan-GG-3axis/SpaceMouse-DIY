import time
import board
import neopixel
import analogio
import digitalio
import rotaryio


PIN_DATOS = board.GP0
NUM_LEDS = 12

anillo = neopixel.NeoPixel(PIN_DATOS, NUM_LEDS, brightness=0.1, auto_write=False)
COLOR_REPOSO = (0, 255, 255) # Azul Cían
COLOR_CLIC = (255, 0, 0)     # Rojo


eje_x = analogio.AnalogIn(board.GP26)
eje_y = analogio.AnalogIn(board.GP27)
boton_joy = digitalio.DigitalInOut(board.GP22)
boton_joy.direction = digitalio.Direction.INPUT
boton_joy.pull = digitalio.Pull.UP


encoder = rotaryio.IncrementalEncoder(board.GP15, board.GP14) # si al girar  la derecha el valor es negativo solo cmabiar el orden PG15, Gp14
ultima_posicion = encoder.position

print("¡Sistema Master SpaceMouse Iniciado!")
print("Esperando movimiento...")

while True:

    val_x = eje_x.value
    val_y = eje_y.value
    pos_encoder = encoder.position
    

    if not boton_joy.value: 
        estado_boton = "CLIC!"
        anillo.fill(COLOR_CLIC)
    else:
        estado_boton = "Suelto"
        anillo.fill(COLOR_REPOSO)
        
    anillo.show() # Actualizamos el color del anillo


    print(f"Joystick -> X: {val_x:05d} | Y: {val_y:05d} || Encoder -> Giro: {pos_encoder} || Botón: {estado_boton}")
    
    time.sleep(0.05)