import pygame
import numpy as np
from pygame import surfarray

# Pygameの初期化
pygame.init()

# サーフェスの作成（640x480ピクセル）
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 新しいサーフェスを作成（100x100ピクセル）
surface = pygame.Surface((100, 100))

# surfaceに色を塗る（緑色）
surface.fill((0, 255, 0))  # 緑色で塗りつぶし

# サーフェスを2D配列に変換
array = surfarray.array2d(surface)

# NumPy配列の中身を表示
print(array)

# 結果を確認するために一時的にウィンドウを表示
screen.blit(surface, (270, 190))  # 画面にsurfaceを描画
pygame.display.flip()

# 画面が閉じるまで待機
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
