# textをマイクラ、ウィンドウに表示する
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

import pygame
from lcd_font_mc import LCD_font  # lcd_font_mc が fonts/font.txt を読み込む

pygame.init()

# lcd_font_mc と同じ形式で表示する
display1 = LCD_font(mc)
display1.init_col(BLOCK_INTV=10, COLOR_ON=param.BLACK_WOOL, COLOR_OFF=param.AIR)
display1.init_row(X_ORG=8, Y_ORG=-22, COL_INTV=6)

mc.postToChat('font image display (lcd_font_mc format)')

# 表示するテキスト（16 列に収まるようにする）
text = 'Hello, world!abcdefghijklmno'
# 16 列分だけ表示（必要ならスライスを変更）
for i, ch in enumerate(text[:100]):
    display1.update_col(col=i, code=ord(ch))

# ウィンドウ（pygame）をそのまま維持して終了を待つ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()