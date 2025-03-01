import sys
from datetime import datetime
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

# 数字を表現するための7セグメントディスプレイのパターン
SEGMENTS = {
    '0': [1, 1, 1, 1, 1, 1, 0],
    '1': [0, 1, 1, 0, 0, 0, 0],
    '2': [1, 1, 0, 1, 1, 0, 1],
    '3': [1, 1, 1, 1, 0, 0, 1],
    '4': [0, 1, 1, 0, 0, 1, 1],
    '5': [1, 0, 1, 1, 0, 1, 1],
    '6': [1, 0, 1, 1, 1, 1, 1],
    '7': [1, 1, 1, 0, 0, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1],
    '9': [1, 1, 1, 1, 0, 1, 1]
}

# 7セグメントディスプレイの各セグメントの相対位置
SEGMENT_POSITIONS = [
    (0, 1), (1, 2), (2, 1), (1, 0), (0, -1), (-1, 0), (0, 0)
]

def display_digit(digit, x, y, z):
    pattern = SEGMENTS[digit]
    for i, segment in enumerate(pattern):
        if segment:
            dx, dy = SEGMENT_POSITIONS[i]
            mc.setBlock(x + dx, y + dy, z, param.GLOWSTONE)

def display_time():
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second

        # 時間を表示
        display_digit(str(hour // 10), po.x, po.y, po.z)
        display_digit(str(hour % 10), po.x + 4, po.y, po.z)
        # コロンを表示
        mc.setBlock(po.x + 8, po.y + 1, po.z, param.GLOWSTONE)
        mc.setBlock(po.x + 8, po.y - 1, po.z, param.GLOWSTONE)
        # 分を表示
        display_digit(str(minute // 10), po.x + 10, po.y, po.z)
        display_digit(str(minute % 10), po.x + 14, po.y, po.z)
        # コロンを表示
        mc.setBlock(po.x + 18, po.y + 1, po.z, param.GLOWSTONE)
        mc.setBlock(po.x + 18, po.y - 1, po.z, param.GLOWSTONE)
        # 秒を表示
        display_digit(str(second // 10), po.x + 20, po.y, po.z)
        display_digit(str(second % 10), po.x + 24, po.y, po.z)

        time.sleep(1)

# 時計を表示
display_time()