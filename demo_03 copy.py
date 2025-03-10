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
display1.init_col(BLOCK_INTV=10, COLOR_ON=param.GOLD_BLOCK, COLOR_OFF=param.AIR)
display1.init_row(X_ORG=8, Y_ORG=22, COL_INTV=6)

## 上から２つ目
#display2 = LCD_font(screen)
#display2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=YELLOW, COLOR_OFF=GRAY)
#display2.init_row(X_ORG=2, Y_ORG=18, COL_INTV=6)

## 上から１つ目
#display3 = Seven_seg(screen)
#display3.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=(120, 200, 250), COLOR_OFF=GRAY)
#display3.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)


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
        display1.update_col(col=9, code=int(str(dt_now.day)[0]) + 48)

        #display2.update_col(col=0, code=dt_now.hour // 10 + 48)
        #display2.update_col(col=1, code=dt_now.hour % 10 + 48)
        #display2.update_col(col=2, code=10 + 48)
        #display2.update_col(col=3, code=dt_now.minute // 10 + 48)
        #display2.update_col(col=4, code=dt_now.minute % 10 + 48)
        #display2.update_col(col=5, code=10 + 48)
        #display2.update_col(col=6, code=dt_now.second // 10 + 48)
        #display2.update_col(col=7, code=dt_now.second % 10 + 48)


        #display3.disp_num2(zfil=False, rjust=3, num=count, base=10)

        #display3.disp_num2(zfil=True, rjust=6, num=time_now, base=10)

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()
print()