from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
x=10
y=20
z=10
mc.player.setTilePos(x,y,z)
time.sleep(3)

while True:
    time.sleep(1)
    pos=mc.player.getTilePos()
    mc.postToChat("pos"+"x:"+str(pos.x)+"y"+str(pos.y)+"z"+str(pos.z))
