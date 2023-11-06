# April 2013 Chris Glew Ltd. www.chrisglew.com
# Unhide the 'scene' lines to include the creation of a scene when the scipt is run

import nuke

def camAim(): 
    cam = nuke.nodes.Camera() 
    aim = nuke.nodes.Axis() 
#    scene = nuke.nodes.Scene()

    aim['translate'].setValue(2, 2)

    cam['rotate'].setExpression('degrees(atan2('+aim.name()+'.translate.y-translate.y,sqrt(pow('+aim.name()+'.translate.x-translate.x,2)+pow('+aim.name()+'.translate.z-translate.z,2))))',0) 

    cam['rotate'].setExpression(aim.name()+'.translate.z-this.translate.z >= 0 ? 180+degrees(atan2('+aim.name()+'.translate.x-translate.x,'+aim.name()+'.translate.z-translate.z)):180+degrees(atan2('+aim.name()+'.translate.x-translate.x,'+aim.name()+'.translate.z-translate.z))',1) 

#    scene.setInput(0, aim) 
#    scene.setInput(1, cam)