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

mc.setBlock(0, 0, 0,  param.OAK_LOG)
mc.setBlock(0, 1, 0,  param.OAK_LOG)
mc.setBlock(0, 2, 0,  param.OAK_LOG)
mc.setBlock(0, 3, 0,  param.OAK_LOG)
mc.setBlock(1, 3, 0,  param.OAK_LEAVES)
mc.setBlock(0, 3, 1,  param.OAK_LEAVES)
mc.setBlock(-1, 3, 0,  param.OAK_LEAVES)
mc.setBlock(0, 3, -1,  param.OAK_LEAVES)
mc.setBlock(1, 3, 1,  param.OAK_LEAVES)
mc.setBlock(-1, 3, -1,  param.OAK_LEAVES)
mc.setBlock(1, 3, -1,  param.OAK_LEAVES)
mc.setBlock(-1, 3, 1,  param.OAK_LEAVES)
mc.setBlock(0, 3, 0,  param.OAK_LEAVES)

