# やってみたいtest
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


mc.postToChat('木')

y = 63

# オーク→1
# トウヒ→2
# シラカバ→3
# ジャングル→4
# アカシア→5
# ダークオーク→6
# マングローブ→7
# サクラ→8
# ツツジ→9
# ペールオーク→10
type = 1
# 普通のオーク(長い)→1
# 普通のオーク(短い)→2
# オークの巨木→3
category = 1
if type == 1:
    if category == 1:
        mc.setBlocks(0, 0+y, 0, 0, 6+y, 0, param.OAK_LOG)