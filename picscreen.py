import RPi.GPIO as GPIO
import DEV_Config
import OLED_Driver
import time

from PIL import Image,ImageDraw,ImageFont

#try:
def start():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('start.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_one_start():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_one_start.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_one_maxbright():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_one_maxbright.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_one_processing():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_one_processing.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_one_success():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_one_success.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_one_fail():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_one_fail.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_one_timeout():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_one_timeout.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_two_start():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_two_start.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_two_movedown():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_two_movedown.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_two_moveup():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_two_moveup.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_two_processing():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_two_processing.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_two_success():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_two_success.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_two_fail():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_two_fail.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_two_timeout():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_two_timeout.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_three_start():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_three_start.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_three_indexfinger():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_three_indexfinger.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_three_notmove():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_three_notmove.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_three_processing():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_three_processing.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_three_success():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_three_success.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_three_fail():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_three_fail.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def step_three_timeout():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('step_three_timeout.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)

def alldone():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('alldone.BMP')#this pis is small ,Will trigger an exception,but you can show
    OLED.OLED_ShowImage(image,0,0)







def destroy():
	GPIO.cleanup()                     # Release resource
	
if __name__ == '__main__':
    try:
        alldone()
    except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destory()
    finally:
        GPIO.cleanup() # cleanup all GPIO