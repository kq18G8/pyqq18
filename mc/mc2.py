from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
x=10
y=20
z=10
mc.player.setTilePos(x,y,z)
time.sleep(3)
x=20
y=50
z=15
mc.player.setTilePos(x,y,z)
time.sleep(3)
x=30
y=30
z=5
mc.player.setTilePos(x,y,z)

                              
