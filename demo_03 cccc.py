# msgをマイクラ世界に書く
import sys

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po

# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)
# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
from lcd_font_mc import LCD_font

pygame.init()

clock = pygame.time.Clock()

display1 = LCD_font(mc)
display1.init_col(BLOCK_INTV=10, COLOR_ON=param.SNOW_BLOCK, COLOR_OFF=param.AIR)
display1.init_row(X_ORG=8, Y_ORG=-22, COL_INTV=6)

display1.update_col(col=0, code=5)
display1.update_col(col=1, code=5)
display1.update_col(col=2, code=5)
display1.update_col(col=3, code=5)
display1.update_col(col=4, code=5)
display1.update_col(col=5, code=5)
display1.update_col(col=6, code=5)
display1.update_col(col=7, code=5)
display1.update_col(col=8, code=5)
display1.update_col(col=9, code=5)
display1.update_col(col=10, code=5)
display1.update_col(col=11, code=5)
display1.update_col(col=12, code=5)
display1.update_col(col=13, code=5)
display1.update_col(col=14, code=5)
display1.update_col(col=15, code=5)

running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break


        msg = "Hello, world!"
        if len(msg) == 0:
            print("msg is empty")
        elif len(msg) <= 16:
            for i in range(len(msg)):
                display1.update_col(col=i, code=ord(msg[i]))
        else:
            print("msg is too long")


        clock.tick(20)  # FPS, Frame Per Second
# infinit loop bottom ----

pygame.quit()
print()