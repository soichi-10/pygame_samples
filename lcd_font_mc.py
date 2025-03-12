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
# handmade LCD font for pygame
# 5x7ドットマトリクス

# from math import log
import pygame
from pygame.locals import Rect

# ステップ４
with open("fonts/font.txt", encoding="utf-8") as f:
        LCD_font_styles = f.read().split('\n')


class LCD_font():
    def __init__(self, mc):
        self.mc = mc

    def init_col(self, BLOCK_INTV=4, COLOR_ON=param.GOLD_BLOCK, COLOR_OFF=param.AIR):
        # ひと桁、コラムの設定
        # ブロックのサイズと配置間隔をピクセル指定（インターバル）
        self.BLOCK_INTV = BLOCK_INTV
        # on/offのカラー
        self.COLOR_ON = COLOR_ON
        self.COLOR_OFF = COLOR_OFF

    def init_row(self, X_ORG=2, Y_ORG=8, COL_INTV=6):  # 表示行の設定
        # xy空間での7セグ表示、最上位桁の左下座標をブロック数で指定
        self.X_ORG = X_ORG * self.BLOCK_INTV
        self.Y_ORG = Y_ORG * self.BLOCK_INTV
        # 各桁のブロック間隔をブロック数で指定（インターバル）
        self.COL_INTV = COL_INTV * self.BLOCK_INTV

    def update_col(self, col=0, code=2):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        i = 0
        for y in range(7):
            for x in range(5):
                if LCD_font_styles[code * 7 + y][x] == "1":
                    color = self.COLOR_ON
                else:
                    color = self.COLOR_OFF
                # 桁の原点
                x0 = self.X_ORG + self.COL_INTV * col
                y0 = self.Y_ORG
                # ドットの原点座標
                org1 = (((x0 + x * self.BLOCK_INTV -400) // 10),-((y0 + y * self.BLOCK_INTV -150 )// 10) + 100,po.z -200)
                # ドットを描く
                self.mc.setBlock(org1[0], org1[1], org1[2] + 10, color)
                i += 1

                
print()