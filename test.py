import sys
import time
import pygame
import mss
import numpy as np
import win32gui

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po

# Connect to Minecraft
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if "Error" in result:
    sys.exit(result)
else:
    print(result)

mc.postToChat('UFO')

ws, ad, xz = 0, 0, -10

def build_ufo(ws, ad, xz):
    mc.setBlock(-1 + ws, 180 + xz, -1 + ad, param.GOLD_BLOCK)
    mc.setBlock(-1 + ws, 180 + xz, 1 + ad, param.GOLD_BLOCK)
    mc.setBlock(1 + ws, 180 + xz, -1 + ad, param.GOLD_BLOCK)
    mc.setBlock(1 + ws, 180 + xz, 1 + ad, param.GOLD_BLOCK)
    mc.setBlocks(-1 + ws, 181 + xz, -1 + ad, 1 + ws, 181 + xz, 1 + ad, param.IRON_BLOCK)
    mc.setBlocks(-1 + ws, 183 + xz, -1 + ad, 1 + ws, 183 + xz, 1 + ad, param.IRON_BLOCK)
    mc.setBlock(1 + ws, 182 + xz, 0 + ad, param.GLASS)
    mc.setBlock(-1 + ws, 182 + xz, 0 + ad, param.GLASS)
    mc.setBlock(0 + ws, 182 + xz, 1 + ad, param.GLASS)
    mc.setBlock(0 + ws, 182 + xz, -1 + ad, param.GLASS)

def delete_ufo(ws, ad, xz):
    mc.setBlocks(-1 + ws, 180 + xz, -1 + ad, 1 + ws, 183 + xz, 1 + ad, param.AIR)

# 初期UFO作成
build_ufo(ws, ad, xz)

# Pygame初期化
pygame.init()
print("Pygame initialized")  # 初期化確認
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption('UFO Control')

def get_minecraft_window():
    """ Minecraftウィンドウの位置とサイズを取得 """
    def enum_windows_callback(hwnd, windows):
        title = win32gui.GetWindowText(hwnd)
        if "Minecraft" in title:  # タイトルに "Minecraft" を含むウィンドウを探す
            windows.append(hwnd)

    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)

    if windows:
        hwnd = windows[0]  # 最初に見つかったウィンドウを使用
        rect = win32gui.GetWindowRect(hwnd)
        return {"top": rect[1], "left": rect[0], "width": rect[2] - rect[0], "height": rect[3] - rect[1]}
    return None

def capture_minecraft_screen():
    """Minecraftのウィンドウ部分のみキャプチャ"""
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # 1番目のモニターをキャプチャ
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)[:, :, :3]  # BGR → RGB に変換

        # 画像サイズを確認
        print(f"Image shape: {img.shape}")  # 画像の形状を確認

        # **Pygame Surface に変換**
        img_surface = pygame.surfarray.make_surface(img)
        img_surface = pygame.transform.scale(img_surface, (1000, 750))  # **画面サイズにリサイズ**
        img_surface = img_surface.convert()  # **不要な透明情報を削除**
        
        return img_surface

def infinite_loop():
    global ws, ad, xz
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: delete_ufo(ws, ad, xz); ws += 1; build_ufo(ws, ad, xz)
        if keys[pygame.K_s]: delete_ufo(ws, ad, xz); ws -= 1; build_ufo(ws, ad, xz)
        if keys[pygame.K_a]: delete_ufo(ws, ad, xz); ad -= 1; build_ufo(ws, ad, xz)
        if keys[pygame.K_d]: delete_ufo(ws, ad, xz); ad += 1; build_ufo(ws, ad, xz)
        if keys[pygame.K_x]: delete_ufo(ws, ad, xz); xz += 1; build_ufo(ws, ad, xz)
        if keys[pygame.K_z]: delete_ufo(ws, ad, xz); xz -= 1; build_ufo(ws, ad, xz)

        # **前のフレームを完全にクリア**
        screen.fill((0, 0, 0))  
        
        # **Minecraftのスクリーンショットを取得して表示**
        minecraft_screen = capture_minecraft_screen()
        if minecraft_screen:
            screen.blit(minecraft_screen, (0, 0))  # **Pygame の画面の左上に描画**
        else:
            print("No screen captured")

        pygame.display.update()  # **画面更新**
        time.sleep(0.1)  # 0.1秒待機

    pygame.quit()  # Pygame終了

try:
    infinite_loop()
except KeyboardInterrupt:
    pygame.quit()
