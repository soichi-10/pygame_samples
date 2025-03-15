# demo for text display by freetype
# pygame.freetype module is a replacement for pygame.font
# for loading and rendering fonts.
# freefontは、fontを置き換えるもの。こっちを使いましょう。

import pygame
import pygame.freetype
import numpy as np
from pygame import surfarray


BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()
screen = pygame.display.set_mode((320, 120))  # display Surfaceの生成。
pygame.display.set_caption('freetype demo')

# font1: Fontオブジェクト。指定文字サイズで全文字のビットマップデータをレンダリングして作成。
# text1: Surfaceオブジェクト。Fontオブジェクトから必要な文字のビットマップデータを切り出して作成。
# screen: display Surfaceオブジェクト。ウィンドウになる。
# font1から、text1を作り(render)、screenに複写(blit)する。


# フォントファイルを指定する場合
# font1 = pygame.freetype.Font('hack-fonts/Hack-Regular.ttf', 36)
# システムにインストールされているフォントの名前を指定する場合
# font1 = pygame.freetype.SysFont('natume', 18)
font1 = pygame.freetype.Font('fonts/misaki_gothic.ttf', 50)

screen.fill(WHITE)

# スクリーンに直接render_toする方法
font1.antialiased = False  # アンチエイリアス、文字の平滑化は行わない。
font1.render_to(screen, (20, 48), 'こんにちは', (BLACK))

# レンダリングされた結果を反映
pygame.display.flip()

array = surfarray.array2d(screen)
with open('output.txt', 'w') as file:
    for row in array:
        for pixel in row:
            # 16進数からRGBに分解
            red = (pixel >> 16) & 0xFF
            green = (pixel >> 8) & 0xFF
            blue = pixel & 0xFF
            # RGB値をファイルに書き込む（改行付き）
            file.write(f"({red}, {green}, {blue})\n")  # 各RGB値の後に改行を追加

# 何もしない無限ループ。ctrl-cやウィンドウを閉じたときの終了処理のみ。
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
