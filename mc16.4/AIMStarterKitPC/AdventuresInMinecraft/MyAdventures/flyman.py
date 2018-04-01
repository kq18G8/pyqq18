from mcpi.minecraft import Minecraft
import time

print("hello world")

mc=Minecraft.create()
x=10
y=20
z=10
mc.player.setTilePos(x,y,z)
time.sleep(3)

print("hello world1")

mc=Minecraft.create()
x=10
y=100
z=10
mc.player.setTilePos(x,y,z)
time.sleep(3)

mc=Minecraft.create()
x=10
y=100
z=100
mc.player.setTilePos(x,y,z)
time.sleep(3)
