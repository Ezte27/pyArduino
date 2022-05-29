import time
import serial
import pygame

# pygame stuff
width = 800
height = 600

bar_width = 341
bar_height = 20
bar3_width = 34.1

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((250, 250, 250))
pygame.display.set_caption('Potentiometer')

bar_surface = pygame.Surface((bar_width, bar_height))
bar_surface.fill((200, 200, 200))
bar_rect = bar_surface.get_rect(center = ((width//2), (height//2)))

bar2_surface = pygame.Surface((bar_width, bar_height))
bar2_surface.fill((20, 20, 230))
bar2_rect = bar2_surface.get_rect(topleft = ((width//2)-(bar_width//2), (height//2)-(bar_height//2)))

bar3_surface = pygame.Surface((bar3_width, bar_height))
bar3_surface.fill((30, 30, 30))
bar3_rect = bar3_surface.get_rect(topleft = (((width//2)-(bar_width//2)) + 204.6, (height//2)-(bar_height*1.5)))

arduinoData = serial.Serial('com3', 115200)
data = 0
voltage = 0
time.sleep(1) # To wait for the object 'arduinoData' to load correctly

running = True
while running:

    #pygame stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    bar2_surface = pygame.transform.scale(bar2_surface, (voltage//3, bar_height)) 
    bar2_surface.fill((20, 20, 230))
    bar3_surface.fill((30, 30, 30))

    if 613.8 <= voltage <= 716.1:
        bar3_surface.fill((230, 20, 20))

    screen.blit(bar_surface, bar_rect)
    screen.blit(bar2_surface, bar2_rect)
    screen.blit(bar3_surface, bar3_rect)
    pygame.display.update()


    while arduinoData.inWaiting == 0:
        pass

    data = (str(arduinoData.readline(), 'utf-8')).strip('\r\n')
    voltage = float((data.split(':'))[1])
    print(voltage)
    time.sleep(0.01)