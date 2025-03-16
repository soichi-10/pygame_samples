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
import pygame.freetype
from pygame import surfarray

# 色設定
BLACK = (0, 0, 0)  # 黒
WHITE = (255, 255, 255)  # 白

pygame.init()

# フォントを設定
font1 = pygame.freetype.Font('fonts/misaki_gothic.ttf', 16)

# テキストを設定
text = 'こんにちは'

# テキストのサイズを取得
text_rect = font1.get_rect(text)
width, height = text_rect.width, text_rect.height

# ウィンドウサイズをテキストぴったりにする
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('freetype demo')

# 背景を白で塗る
screen.fill(WHITE)

# テキストを (0, 0) に描画
font1.render_to(screen, (0, 0), text, BLACK)

# 画面を更新
pygame.display.flip()

# サーフェスのグレースケールデータを取得
array = surfarray.array2d(screen)  # これでscreenからグレースケールデータを取得

array_height, array_width = array.shape  # arrayのサイズを取得

mc.postToChat('font image display')
for y in range(array_height):
    for x in range(array_width):
        set_x = (y - width //2)
        set_y = (x * -1 + 120)
        mc.setBlock(set_x, set_y, 0, param.BLACK_WOOL if array[y][x] == 0 else param.AIR)
        
print(f"/tp {set_x - 100} {set_y} {po.z}")

# 何もしない無限ループ。ウィンドウを閉じると終了
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()