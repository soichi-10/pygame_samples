# WASD Shict Spaceで操作できるUFOをマイクラ世界に出す
import sys
import time
import pygame

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

mc.postToChat('UFO')

ws = 0
ad = 0
xz = 100

def build_ufo(ws, ad, xz):
    mc.setBlock(-1 + ws, 0 + xz, -1 + ad, param.GOLD_BLOCK)
    mc.setBlock(-1 + ws, 0 + xz, 1 + ad, param.GOLD_BLOCK)
    mc.setBlock(1 + ws, 0 + xz, -1 + ad, param.GOLD_BLOCK)
    mc.setBlock(1 + ws, 0 + xz, 1 + ad, param.GOLD_BLOCK)

    mc.setBlocks(-1 + ws, 1 + xz, -1 + ad, 1 + ws, 1 + xz, 1 + ad, param.IRON_BLOCK)
    mc.setBlock(-1 + ws, 2 + xz, -1 + ad, param.IRON_BLOCK)
    mc.setBlock(-1 + ws, 2 + xz, 1 + ad, param.IRON_BLOCK)
    mc.setBlock(1 + ws, 2 + xz, -1 + ad, param.IRON_BLOCK)
    mc.setBlock(1 + ws, 2 + xz, 1 + ad, param.IRON_BLOCK)
    mc.setBlocks(-1 + ws, 3 + xz, -1 + ad, 1 + ws, 3 + xz, 1 + ad, param.IRON_BLOCK)

    mc.setBlock(1 + ws, 2 + xz, 0 + ad, param.GLASS)
    mc.setBlock(-1 + ws, 2 + xz, 0 + ad, param.GLASS)
    mc.setBlock(0 + ws, 2 + xz, 1 + ad, param.GLASS)
    mc.setBlock(0 + ws, 2 + xz, -1 + ad, param.GLASS)

def delete_ufo(ws, ad, xz):
    mc.setBlocks(-1 + ws, 0 + xz, -1 + ad, 1 + ws, 3 + xz, 1 + ad, param.AIR)

# 初期のUFOを作成
build_ufo(ws, ad, xz)

# Pygameの初期化
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('UFO Control')

def infinite_loop():
    global ws, ad, xz
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            delete_ufo(ws, ad, xz)
            ws += 1
            build_ufo(ws, ad, xz)
            print(f"{po.x + ws} {po.y + xz} {po.z + ad}")
        if keys[pygame.K_s]:
            delete_ufo(ws, ad, xz)
            ws -= 1
            build_ufo(ws, ad, xz)
            print(f"{po.x + ws} {po.y + xz} {po.z + ad}")
        if keys[pygame.K_a]:
            delete_ufo(ws, ad, xz)
            ad -= 1
            build_ufo(ws, ad, xz)
            print(f"{po.x + ws} {po.y + xz} {po.z + ad}")
        if keys[pygame.K_d]:
            delete_ufo(ws, ad, xz)
            ad += 1
            build_ufo(ws, ad, xz)
            print(f"{po.x + ws} {po.y + xz} {po.z + ad}")
        if keys[pygame.K_x]:
            delete_ufo(ws, ad, xz)
            xz += 1
            build_ufo(ws, ad, xz)
            print(f"{po.x + ws} {po.y + xz} {po.z + ad}")
        if keys[pygame.K_SPACE]:
            delete_ufo(ws, ad, xz)
            xz += 1
            build_ufo(ws, ad, xz)
            print(f"{po.x + ws} {po.y + xz} {po.z + ad}")
        if keys[pygame.K_z]:
            delete_ufo(ws, ad, xz)
            xz -= 1
            build_ufo(ws, ad, xz)
            print(f"{po.x + ws} {po.y + xz} {po.z + ad}")
        if keys[pygame.K_LCTRL]:
            delete_ufo(ws, ad, xz)
            xz -= 1
            build_ufo(ws, ad, xz)
            print(f"{po.x + ws} {po.y + xz} {po.z + ad}")
        if keys[pygame.K_LSHIFT]:
            delete_ufo(ws, ad, xz)
            xz -= 1
            build_ufo(ws, ad, xz)
            print(f"{po.x + ws} {po.y + xz} {po.z + ad}")

        time.sleep(0.1)  # 0.1秒待機

try:
    infinite_loop()
except KeyboardInterrupt:
    pygame.quit()