from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

stayed_time=0

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("pos"+"x"+str(pos.x)+"y"+str(pos.y)+"z"+str(pos.z)) 
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
        
     
