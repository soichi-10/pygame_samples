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

## 上から３つ目
display1 = LCD_font(mc)
display1.init_col(BLOCK_INTV=10, COLOR_ON=param.SNOW_BLOCK, COLOR_OFF=param.AIR)
display1.init_row(X_ORG=8, Y_ORG=22, COL_INTV=6)

## 上から２つ目
display2 = LCD_font(mc)
display2.init_col(BLOCK_INTV=10, COLOR_ON=param.SNOW_BLOCK, COLOR_OFF=param.AIR)
display2.init_row(X_ORG=8, Y_ORG=0, COL_INTV=6)

## 上から１つ目
display3 = LCD_font(mc)
display3.init_col(BLOCK_INTV=10, COLOR_ON=param.SNOW_BLOCK, COLOR_OFF=param.AIR)
display3.init_row(X_ORG=8, Y_ORG=-22, COL_INTV=6)

mc.postToChat('文字表示')

display3.update_col(col=0, code=5)
display3.update_col(col=1, code=5)
display3.update_col(col=2, code=5)
display3.update_col(col=3, code=5)
display3.update_col(col=4, code=5)
display3.update_col(col=5, code=5)
display3.update_col(col=6, code=5)
display3.update_col(col=7, code=5)
display3.update_col(col=8, code=5)
display3.update_col(col=9, code=5)
display3.update_col(col=10, code=5)
display3.update_col(col=11, code=5)
display3.update_col(col=12, code=5)
display3.update_col(col=13, code=5)
display3.update_col(col=14, code=5)
display3.update_col(col=15, code=5)

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
        # 「for count」のループから抜ける。whileループも抜ける。

        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)
        date_now = (dt_now.year * 10000
                    + dt_now.month * 100
                    + dt_now.day)

        display1.update_col(col=0, code=int(str(dt_now.year)[0]) + 48)
        display1.update_col(col=1, code=int(str(dt_now.year)[1]) + 48)
        display1.update_col(col=2, code=int(str(dt_now.year)[2]) + 48)
        display1.update_col(col=3, code=int(str(dt_now.year)[3]) + 48)
        display1.update_col(col=4, code=(ord('-')))
        display1.update_col(col=5, code=dt_now.month // 10 + 48)
        display1.update_col(col=6, code=int(str(dt_now.month)[0]) + 48)
        display1.update_col(col=7, code=(ord('-')))
        display1.update_col(col=8, code=dt_now.day // 10 + 48)
        display1.update_col(col=9, code=int(str(dt_now.day)[1]) + 48)

        display2.update_col(col=0, code=dt_now.hour // 10 + 48)
        display2.update_col(col=1, code=dt_now.hour % 10 + 48)
        display2.update_col(col=2, code=10 + 48)
        display2.update_col(col=3, code=dt_now.minute // 10 + 48)
        display2.update_col(col=4, code=dt_now.minute % 10 + 48)
        display2.update_col(col=5, code=10 + 48)
        display2.update_col(col=6, code=dt_now.second // 10 + 48)
        display2.update_col(col=7, code=dt_now.second % 10 + 48)

        msg = "dekita--"
        if len(msg) == 0:
            print("msg is empty")
        elif len(msg) == 1:
            display3.update_col(col=0, code=ord(str(msg)[0]))
        elif len(msg) == 2:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
        elif len(msg) == 3:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
        elif len(msg) == 4:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
        elif len(msg) == 5:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
        elif len(msg) == 6:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
        elif len(msg) == 7:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
        elif len(msg) == 8:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
            display3.update_col(col=7, code=ord(str(msg)[7]))
        elif len(msg) == 9:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
            display3.update_col(col=7, code=ord(str(msg)[7]))
            display3.update_col(col=8, code=ord(str(msg)[8]))
        elif len(msg) == 10:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
            display3.update_col(col=7, code=ord(str(msg)[7]))
            display3.update_col(col=8, code=ord(str(msg)[8]))
            display3.update_col(col=9, code=ord(str(msg)[9]))
        elif len(msg) == 11:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
            display3.update_col(col=7, code=ord(str(msg)[7]))
            display3.update_col(col=8, code=ord(str(msg)[8]))
            display3.update_col(col=9, code=ord(str(msg)[9]))
            display3.update_col(col=10, code=ord(str(msg)[10]))
        elif len(msg) == 12:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
            display3.update_col(col=7, code=ord(str(msg)[7]))
            display3.update_col(col=8, code=ord(str(msg)[8]))
            display3.update_col(col=9, code=ord(str(msg)[9]))
            display3.update_col(col=10, code=ord(str(msg)[10]))
            display3.update_col(col=11, code=ord(str(msg)[11]))
        elif len(msg) == 13:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
            display3.update_col(col=7, code=ord(str(msg)[7]))
            display3.update_col(col=8, code=ord(str(msg)[8]))
            display3.update_col(col=9, code=ord(str(msg)[9]))
            display3.update_col(col=10, code=ord(str(msg)[10]))
            display3.update_col(col=11, code=ord(str(msg)[11]))
            display3.update_col(col=12, code=ord(str(msg)[12]))
        elif len(msg) == 14:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
            display3.update_col(col=7, code=ord(str(msg)[7]))
            display3.update_col(col=8, code=ord(str(msg)[8]))
            display3.update_col(col=9, code=ord(str(msg)[9]))
            display3.update_col(col=10, code=ord(str(msg)[10]))
            display3.update_col(col=11, code=ord(str(msg)[11]))
            display3.update_col(col=12, code=ord(str(msg)[12]))
            display3.update_col(col=13, code=ord(str(msg)[13]))
        elif len(msg) == 15:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
            display3.update_col(col=7, code=ord(str(msg)[7]))
            display3.update_col(col=8, code=ord(str(msg)[8]))
            display3.update_col(col=9, code=ord(str(msg)[9]))
            display3.update_col(col=10, code=ord(str(msg)[10]))
            display3.update_col(col=11, code=ord(str(msg)[11]))
            display3.update_col(col=12, code=ord(str(msg)[12]))
            display3.update_col(col=13, code=ord(str(msg)[13]))
            display3.update_col(col=14, code=ord(str(msg)[14]))
        elif len(msg) == 16:
            display3.update_col(col=0, code=ord(str(msg)[0]))
            display3.update_col(col=1, code=ord(str(msg)[1]))
            display3.update_col(col=2, code=ord(str(msg)[2]))
            display3.update_col(col=3, code=ord(str(msg)[3]))
            display3.update_col(col=4, code=ord(str(msg)[4]))
            display3.update_col(col=5, code=ord(str(msg)[5]))
            display3.update_col(col=6, code=ord(str(msg)[6]))
            display3.update_col(col=7, code=ord(str(msg)[7]))
            display3.update_col(col=8, code=ord(str(msg)[8]))
            display3.update_col(col=9, code=ord(str(msg)[9]))
            display3.update_col(col=10, code=ord(str(msg)[10]))
            display3.update_col(col=11, code=ord(str(msg)[11]))
            display3.update_col(col=12, code=ord(str(msg)[12]))
            display3.update_col(col=13, code=ord(str(msg)[13]))
            display3.update_col(col=14, code=ord(str(msg)[14]))
            display3.update_col(col=15, code=ord(str(msg)[15]))
        else:
            print("msg is too long")


        clock.tick(20)  # FPS, Frame Per Second
# infinit loop bottom ----

pygame.quit()
print()