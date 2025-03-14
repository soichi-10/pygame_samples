import sys
import time

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

## 上から１つ目
display1 = LCD_font(mc)
display1.init_col(BLOCK_INTV=10, COLOR_ON=param.SNOW_BLOCK, COLOR_OFF=param.AIR)
display1.init_row(X_ORG=8, Y_ORG=-22, COL_INTV=6)

mc.postToChat('ticker display')

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

repeat = 0

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

        msg = "A new playground opened in the city yesterday. Many children went there to play. The playground has swings, slides, and a sandbox. It is very big and safe. Parents are happy because it is a good place for their children to play. The children love it!"
        if len(msg) == 0:
            print("msg is empty")
        else:
            start_index = repeat
            end_index = start_index + 16
            for i in range(start_index, min(len(msg), end_index)):
                display1.update_col(col=i - start_index, code=ord(msg[i]))
            if end_index >= len(msg):
                repeat = 0  # メッセージの終わりに達したらリセット
            else:
                repeat += 1
        time.sleep(0.3)


        clock.tick(20)  # FPS, Frame Per Second
# infinit loop bottom ----

pygame.quit()
print()