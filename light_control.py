import time
import RPi.GPIO as GPIO
 
# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
 
 
# Configure the count of pixels:
PIXEL_COUNT = 142
 
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

# Define the wheel function to interpolate between different hues.
def wheel(pos):
    if pos < 85:
        return Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Adafruit_WS2801.RGB_to_color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Adafruit_WS2801.RGB_to_color(0, pos * 3, 255 - pos * 3)
 
# Define rainbow cycle function to do a cycle of all hues.
def rainbow_cycle_successive(wait=0.1):
    for i in range(pixels.count()):
        # tricky math! we use each pixel as a fraction of the full 96-color wheel
        # (thats the i / strip.numPixels() part)
        # Then add in j which makes the colors go around per pixel
        # the % 96 is to make the wheel cycle around
        pixels.set_pixel(i, wheel(((i * 256 // pixels.count())) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)
def rainbow_cycle(wait=0.005):
    for j in range(256): # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((i * 256 // pixels.count()) + j) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)
 
def rainbow_colors(wait=0.05):
    for j in range(256): # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)
			
def decreaseBrightness(step = 20):
	for i in range(pixels.count()):
		r, g, b = pixels.get_pixel_rgb(i)
		r = int(r - step)
		g = int(g - step)
		b = int(b - step)
		pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( r, g, b ))
	print "R: {}, G: {}, B: {}".format(r,g,b)
	pixels.show()
	
def increaseBrightness(step = 20):
	for i in range(pixels.count()):
		r, g, b = pixels.get_pixel_rgb(i)        
		r = int(r + step)
		g = int(g + step)
		b = int(b + step)
		pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( r, g, b ))
	print "R: {}, G: {}, B: {}".format(r,g,b)
	pixels.show()
	
def setColor(RGB):
	r = int(RGB[0])
	g = int(RGB[1])
	b = int(RGB[2])
	for i in range(pixels.count()):
		pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( r, g, b ))
	pixels.show()  # Make sure to call show() after changing any pixels!
	
def clear_pixels():
	pixels.clear()
	pixels.show()