import RPi.GPIO as GPIO
import DEV_Config
import OLED_Driver
import time

from PIL import Image,ImageDraw,ImageFont

#try:
def pic():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)

    image = Image.open('1.bmp')#this pis is small ,Will trigger an exception,but you can show
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
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    ft1 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 18)
    ft2 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 40)
    draw.text((20, 12), 'STEP 1/3', font = ft1, fill = "White")
    draw.text((10, 42), 'Done!', font = ft2, fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)

    #print ("***draw progress bar")
    draw.rectangle([(0,100),(42,120)],fill = "White")
        
    OLED.OLED_ShowImage(image,0,0)
    #DEV_Config.Driver_Delay_ms(10000)

    #image = Image.open('flower.bmp')#this pis is small ,Will trigger an exception,but you can show
    #OLED.OLED_ShowImage(image,0,0)

def step_one_fail():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    draw.text((6, 12), 'Verification failed.', fill = "White")
    draw.text((16, 24), 'Please try again.', fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)
        
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
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    ft1 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 18)
    ft2 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 40)
    draw.text((20, 12), 'STEP 2/3', font = ft1, fill = "White")
    draw.text((10, 42), 'Done!', font = ft2, fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)

    #print ("***draw progress bar")
    draw.rectangle([(0,100),(84,120)],fill = "White")
        
    OLED.OLED_ShowImage(image,0,0)

def step_two_fail_camera():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    draw.text((18, 12), 'Please move the', fill = "White")
    draw.text((4, 24), 'camera following the', fill = "White")
    draw.text((4, 36), 'on-screen directions.', fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)

    #print ("***draw progress bar")
    draw.rectangle([(0,100),(42,120)],fill = "White")
        
    OLED.OLED_ShowImage(image,0,0)

def step_two_fail_nomatch():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    draw.text((6, 12), 'Verification failed.', fill = "White")
    draw.text((16, 24), 'Please try again.', fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)

    #print ("***draw progress bar")
    draw.rectangle([(0,100),(42,120)],fill = "White")
        
    OLED.OLED_ShowImage(image,0,0)

def step_two_fail_timeout():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    draw.text((40, 12), 'Time out.', fill = "White")
    draw.text((16, 24), 'Please try again.', fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)

    #print ("***draw progress bar")
    draw.rectangle([(0,100),(42,120)],fill = "White")
        
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
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    draw.text((20, 12), 'Please put your', fill = "White")
    draw.text((30, 24), 'index finger', fill = "White")
    draw.text((20, 36), 'on the scanner.', fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)

    #print ("***draw progress bar")
    draw.rectangle([(0,100),(84,120)],fill = "White")
        
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
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    ft1 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 18)
    ft2 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 40)
    draw.text((20, 12), 'STEP 3/3', font = ft1, fill = "White")
    draw.text((10, 42), 'Done!', font = ft2, fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)

    #print ("***draw progress bar")
    draw.rectangle([(0,100),(126,120)],fill = "White")
        
    OLED.OLED_ShowImage(image,0,0)

def step_three_fail_nomatch():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    draw.text((6, 12), 'Verification failed.', fill = "White")
    draw.text((16, 24), 'Please try again.', fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)

    #print ("***draw progress bar")
    draw.rectangle([(0,100),(84,120)],fill = "White")
        
    OLED.OLED_ShowImage(image,0,0)

def step_three_fail_timeout():
    OLED = OLED_Driver.OLED()

    #print ("**********Init OLED**********")
    OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    OLED.OLED_Init(OLED_ScanDir)

    #OLED.OLED_Clear()
    DEV_Config.Driver_Delay_ms(20)
    image = Image.new("L", (OLED.OLED_Dis_Column, OLED.OLED_Dis_Page), 0)# grayscale (luminance)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', "White")

    #print ("***draw text")
    draw.text((40, 12), 'Time out.', fill = "White")
    draw.text((16, 24), 'Please try again.', fill = "White")

    #print ("***draw line")
    draw.line([(0,100),(126,100)], fill = "White",width = 2)
    draw.line([(126,100),(126,120)], fill = "White",width = 2)
    draw.line([(126,120),(0,120)], fill = "White",width = 2)
    draw.line([(0,120),(0,100)], fill = "White",width = 2)

    #print ("***draw progress bar")
    draw.rectangle([(0,100),(84,120)],fill = "White")
        
    OLED.OLED_ShowImage(image,0,0)



def destroy():
	GPIO.cleanup()                     # Release resource
	
if __name__ == '__main__':
    try:
        step_three_fail_timeout()
    except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destory()
    finally:
        GPIO.cleanup() # cleanup all GPIO

#except:
#	print("except")
#	GPIO.cleanup()