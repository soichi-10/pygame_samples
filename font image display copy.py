# textをウィンドウに表示しマイクラでも流れる文字を出す
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
text = '最新のポジティブなニュースとして、3月16日に行われた千葉市長選挙で、現職の神谷俊一氏が再選を果たし、新顔2氏を破ったことが報じられています。'

# ウィンドウサイズを設定
screen_width = 16 * 8  # 16文字分の幅
screen_height = 16  # 1文字分の高さ
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ticker Display')
print(screen.get_size())

# 背景を白で塗る
screen.fill(WHITE)

def render_text_segment(text_segment):
    screen.fill(WHITE)
    font1.render_to(screen, (0, 0), text_segment, BLACK)
    pygame.display.flip()
    array = surfarray.array2d(screen)
    return array

def display_text_segment(array, start_x, start_y):
    array_height, array_width = array.shape

    for y in range(array_height):
        for x in range(array_width):
            set_x = (y - 60)
            set_y = (x * -1 + 120)
            mc.setBlock(set_x, set_y, 0, param.BLACK_WOOL if array[y][x] == 0 else param.AIR)
            print(f"Block at ({set_x}, {set_y}, {po.z})")

def clear_text_segment(array, start_x, start_y):
    array_height, array_width = array.shape

    for y in range(array_height):
        for x in range(array_width):
            set_x = start_x + x
            set_y = start_y + y
            mc.setBlock(set_x, set_y, po.z, param.AIR)

# テキストをスクロール表示
running = True
start_x = po.x
start_y = po.y + 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(len(text) - 15):
        text_segment = text[i:i+16]
        array = render_text_segment(text_segment)
        display_text_segment(array, start_x, start_y)
        time.sleep(0.1)  # スクロール速度を調整
        clear_text_segment(array, start_x, start_y)

pygame.quit()