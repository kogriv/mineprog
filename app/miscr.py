# import mcpi_e
from mcpi.minecraft import Minecraft

# port = 25565
address, port = "213.110.56.225", 25565
# address, port = "localhost", 4711
# playerName="4cbc29c0-b06b-3738-bd0f-5a905be23b97"
# playerName=""

# mc = Minecraft.create(address,port)

mc = Minecraft.create(address,port
                      # ,playerName
                      )
# pos = mc.player.getPos()

# print("pos: x:{},y:{},z:{}".format(pos.x,pos.y, pos.z))

mc.postToChat("Сейчас я прыгну")

mc.player.setTilePos(0, 120, 0)


